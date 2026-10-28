#!/usr/bin/env python3
"""
propagate-content-entities.py — derive/append people + organization pages from
captured FLAT-content files: those whose contributors live in YAML `people:` /
`organizations:` arrays (articles, podcasts, bookmarks, recipes, lightning-lessons,
papers). The /add convention propagates `people` on ANY flat capture that carries it.

Sister to propagate-entities.py, which handles reference-HUB files (movies / tv-shows /
music / books) by parsing their `## Who's Involved` body. Hub types are skipped here —
use that script for them.

For each person/org in the YAML, adds an "In My Library" backlink to the entity page.
ADDITIVE + idempotent (never duplicates a backlink). Reuses the hardened
slug / match_key / resolve_entity_path from propagate-entities.py (single source of
truth — the normalize-match dup-guard is shared, not copied, so a variant spelling
appends to the existing page instead of spawning 'Name.md' beside 'Name-Surname.md').

Usage:
  python3 Core/skills/add/propagate-content-entities.py Library/articles/.../"X.md" ...
Run from your OS root.

⚠️ Pass the SPECIFIC files you just added — do NOT glob all of Library/ (older files
may use a pre-lock schema this parser misreads).

(Shares the hardened resolver from propagate-entities.py so variant-spelling dups can't recur.)
"""
import os, re, sys, datetime, importlib.util

# Real casing from disk (see propagate-entities.py: a guessed casing broke backlink paths on Mac)
LIB = next((d for d in os.listdir(".") if d.lower() == "library" and os.path.isdir(d)), "library")
FLAT_TYPES = {"article", "podcast", "bookmark", "recipe", "lightning-lesson", "paper"}
HUB_TYPES = {"movie", "tv-show", "book", "artist"}  # → use propagate-entities.py instead

# reuse the hardened helpers from the sister script (hyphenated filename → importlib)
_pe = os.path.join(os.path.dirname(os.path.abspath(__file__)), "propagate-entities.py")
_spec = importlib.util.spec_from_file_location("propagate_entities", _pe)
pe = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pe)


def parse_yaml_list(text, key):
    """Read a YAML array field in either inline (key: [a, b]) or block (key:\\n  - a) form."""
    m = re.search(r'^' + key + r':\s*\[(.*?)\]', text, re.M)
    if m:
        return [x.strip().strip('"').strip("'") for x in m.group(1).split(",") if x.strip()]
    out = []
    lines = text.splitlines()
    for i, l in enumerate(lines):
        if re.match(r'^' + key + r':\s*$', l):
            for j in range(i + 1, len(lines)):
                mm = re.match(r'^\s*-\s+(.*)$', lines[j])
                if mm:
                    out.append(mm.group(1).strip().strip('"').strip("'"))
                elif lines[j].strip() == "":
                    continue
                else:
                    break
            break
    return out


def h1_title(text, path):
    m = re.search(r'^#\s+(.+)$', text, re.M)
    return m.group(1).strip() if m else os.path.basename(path)[:-3]


def ensure_category(etext, value):
    """Add `value` to the `category:` array, in EITHER shape — inline
    (`category: ["a","b"]`) or block-list (`category:` + `  - a` lines) — and write it
    back inline. Creates it inline after `type:` if absent. Returns (text, changed).

    ⚠️ Handling both shapes is load-bearing, not politeness. Matching inline-only is a
    silent-corruption bug: on a block-list page it reads the values as EMPTY (dropping
    them) and replaces just the `category:` line, orphaning the hyphens into invalid
    YAML. And block-list pages are not rare or malformed — `Core/rules/files.md § YAML`
    tells humans to write arrays that way, so every hand-authored entity page arrives in
    the shape an inline-only match would break. Read-liberal, write-strict: whichever
    shape is read, the write normalizes to inline (the standard for this field)."""
    m = re.search(r'^category:[ \t]*\[(.*?)\][ \t]*$', etext, re.M)
    if m:
        cur = [x.strip().strip('"').strip("'") for x in m.group(1).split(",") if x.strip()]
        if value in cur:
            return etext, False
        newline = "category: [" + ", ".join(f'"{c}"' for c in cur + [value]) + "]"
        return etext[:m.start()] + newline + etext[m.end():], True

    m = re.search(r'^category:[ \t]*\n((?:[ \t]*-[ \t]*\S.*\n?)+)', etext, re.M)
    if m:
        cur = [ln.strip().lstrip("-").strip().strip('"').strip("'")
               for ln in m.group(1).splitlines() if ln.strip()]
        if value in cur:
            return etext, False
        repl = "category: [" + ", ".join(f'"{c}"' for c in cur + [value]) + "]"
        if etext[m.end()-1:m.end()] == "\n":
            repl += "\n"
        return etext[:m.start()] + repl + etext[m.end():], True

    return re.sub(r'^(type:.*)$', r'\1' + f'\ncategory: ["{value}"]', etext, count=1, flags=re.M), True


def propagate(path, stats):
    text = open(path, encoding="utf-8").read()
    tm = re.search(r'^type:\s*(\S+)', text, re.M)
    typ = tm.group(1).strip() if tm else None
    if typ in HUB_TYPES:
        print(f"  ! skip (hub type '{typ}' — use propagate-entities.py): {path}")
        return
    if typ not in FLAT_TYPES:
        print(f"  ! skip (type '{typ}' not a recognized flat-capture type): {path}")
        return
    title = h1_title(text, path)
    for kind, key, folder in (("person", "people", "people"),
                              ("organization", "organizations", "organizations")):
        for name in parse_yaml_list(text, key):
            epath = pe.resolve_entity_path(os.path.join(LIB, folder), name)  # hardened: finds variants, never dups
            # rel is relative to where the entity page actually lives — flat
            # (../{type}/) vs active-contact folder (../../{type}/); also handles
            # nested content paths (e.g. lightning-lessons/_unwatched/Title/Title.md)
            # abspath both sides: relpath() resolves a relative `start` against the CWD, so an
            # absolute path argument (what an AI's tool call usually passes) produced
            # ../../../../… climbing to / and back — machine-specific, and it leaked the full path.
            # realpath, not abspath: /tmp → /private/tmp on macOS, and any symlinked folder,
            # would otherwise leave the two sides disagreeing and reproduce the climb.
            rel = os.path.relpath(os.path.realpath(path), os.path.realpath(os.path.dirname(epath)))
            backlink = f"- [{title}]({pe.url_escape(rel)})"   # parens break a markdown link; see the sister script
            if os.path.exists(epath):
                etext = open(epath, encoding="utf-8").read()
                if pe.url_escape(rel) in etext or rel in etext:   # both spellings, or a re-run duplicates
                    stats["skip"] += 1
                    continue
                if "## In My Library" in etext:
                    head, body = etext.split("## In My Library", 1)
                    lines = body.splitlines(keepends=True)
                    insert_at, i = 1, 1
                    while i < len(lines) and (lines[i].startswith("- ") or lines[i].strip() == ""):
                        if lines[i].startswith("- "):
                            insert_at = i + 1
                        i += 1
                    # newline guard: if the line we insert after lacks a trailing newline,
                    # "".join would concatenate the two list items onto one line.
                    if 0 <= insert_at - 1 < len(lines) and lines[insert_at - 1] and not lines[insert_at - 1].endswith("\n"):
                        lines[insert_at - 1] += "\n"
                    lines.insert(insert_at, backlink + "\n")
                    etext = head + "## In My Library" + "".join(lines)
                else:
                    etext = etext.rstrip() + f"\n\n## In My Library\n{backlink}\n"
                # a lightning-lesson's teacher is an instructor (controlled-vocab `category:`)
                if kind == "person" and typ == "lightning-lesson":
                    etext, _ = ensure_category(etext, "instructor")
                open(epath, "w", encoding="utf-8").write(etext)
                stats["appended"] += 1
            else:
                etype = "person" if kind == "person" else "organization"
                why = "" if kind == "person" else "\n## Why I'm Watching\n*(added later, when interest is real)*\n"
                catline = 'category: ["instructor"]\n' if (kind == "person" and typ == "lightning-lesson") else ""
                content = (
                    f"---\nname: {name}\ntype: {etype}\n{catline}date_added: {datetime.date.today().isoformat()}\n---\n\n"
                    f"# {name}\n\n## In My Library\n{backlink}\n{why}"
                )
                os.makedirs(os.path.dirname(epath), exist_ok=True)  # a fresh system has no people/ or organizations/ yet
                open(epath, "w", encoding="utf-8").write(content)
                stats["created"] += 1


def main():
    stats = {"created": 0, "appended": 0, "skip": 0}
    for p in sys.argv[1:]:
        print(f"· {p}")
        propagate(p, stats)
    print(f"\nDone. Entity pages created: {stats['created']}, "
          f"backlinks appended: {stats['appended']}, already-present (skipped): {stats['skip']}")


if __name__ == "__main__":
    main()
