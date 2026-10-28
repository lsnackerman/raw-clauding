#!/usr/bin/env python3
"""
propagate-entities.py — derive/append entity pages from reference-hub title files.

The /add batch serial-merge step. Reads movie/tv-show/book title files (passed as
args), parses their `## Who's Involved` section, and for every person/org:
  - creates Library/people/{Name}.md or Library/organizations/{Name}.md if new
  - appends a backlink under `## In My Library` if the page exists (idempotent —
    never duplicates a line, never clobbers existing non-screen backlinks)
  - merges the controlled-vocab `category:` index (union across the library)

ADDITIVE by design: entity pages also accumulate backlinks from podcasts/articles,
so this only adds screen/book backlinks, it never regenerates the page.

Usage:
  python3 Core/skills/add/propagate-entities.py Library/movies/"Poor Things.md" ...
Run from your OS root.

⚠️ Pass the SPECIFIC title files you just added — do NOT glob the whole library
(`Library/movies/*.md`). Older entries use varying "Who's Involved" formats this
parser misreads (it can create people-as-orgs and duplicate pages on older-format files).
Only run it over files known to follow the current entry format.
"""
import sys, os, re, unicodedata, datetime

# cwd-relative (script is invoked from your system root); survives relocation
# Use the folder's REAL casing, read from disk. On a Mac, isdir("library") is True
# for a folder named "Library" too, and relpath is purely lexical, so a guessed
# casing gave every backlink a redundant "../../Library/" hop.
LIB = next((d for d in os.listdir(".") if d.lower() == "library" and os.path.isdir(d)), "library")

TYPE_FOLDER = {"movie": "movies", "tv-show": "tv-shows", "book": "books", "artist": "music"}

def url_escape(rel):
    """Percent-escape only the characters that break a markdown link URL. Spaces are
    left alone deliberately — every reader (Obsidian, GitHub, the checkers) handles them.
    Parens are the real breakage: an unescaped "(" / ")" ends the link at the FIRST ")"
    in every renderer, so `[The Mummy (2026)](../movies/The Mummy (2026).md)` renders
    dead while the file sits happily on disk."""
    return rel.replace("(", "%28").replace(")", "%29")

PERSON_ROLES = {"actor","voice-actor","director","writer","creator","composer","cinematographer",
    "editor","animator","artist","author","translator","illustrator","producer","songwriter",
    "guitarist","bassist","drummer","keyboardist","vocalist","engineer","mc","dj","musician"}
ORG_ROLES = {"studio","production-company","distributor","network","label","streamer","publisher","imprint"}

# group header (bolded) -> ("person"|"org", default role vocab)
def classify_group(header):
    h = header.lower()
    if any(k in h for k in ["cast"]):
        return "person", "actor"
    if any(k in h for k in ["studio", "network", "distribut", "publisher", "label"]):
        return "org", None
    if "author" in h:
        return "person", "author"
    if any(k in h for k in ["translator", "illustrator", "editor"]):
        return "person", None
    # Creative / Creators / etc.
    return "person", None

def role_vocab(group_default, suffix, kind="person"):
    """Map the '— suffix' text to controlled roles vocab (may be several)."""
    s = suffix.lower()
    roles = []
    if group_default == "actor":
        roles.append("voice-actor" if ("voice" in s) else "actor")
        if "also producer" in s or "producer)" in s:
            roles.append("producer")
        return roles
    if group_default == "author":
        return ["author"]
    # crew / org — keyword scan
    kw = [
        ("director of photography", "cinematographer"),
        ("cinematograph", "cinematographer"),
        ("showrunner", "producer"),
        ("director", "director"),
        ("screenplay", "writer"),
        ("co-writer", "writer"),
        ("writer", "writer"),
        ("story", "writer"),
        ("creator", "creator"),
        ("composer", "composer"),
        ("editor", "editor"),
        ("animator", "animator"),
        ("production design", "artist"),
        ("costume design", "artist"),
        ("concept", "artist"),
        ("visual design", "artist"),
        ("illustrator", "illustrator"),
        ("translator", "translator"),
        # music people
        ("songwriter", "songwriter"),
        ("guitar", "guitarist"),
        ("bass", "bassist"),
        ("drum", "drummer"),
        ("keyboard", "keyboardist"),
        ("vocal", "vocalist"),
        ("singer", "vocalist"),
        ("pian", "keyboardist"),
        ("engineer", "engineer"),
        ("co-production", "producer"),
        ("production", "producer"),
        ("producer", "producer"),
        # org roles
        ("distributor", "distributor"),
        ("network", "network"),
        ("streamer", "streamer"),
        ("imprint", "imprint"),
        ("publisher", "publisher"),
        ("label", "label"),
        ("production company", "production-company"),
        ("production", "production-company"),
        ("studio", "studio"),
        ("co-financier", "production-company"),
    ]
    for needle, vocab in kw:
        if needle in s and vocab not in roles:
            roles.append(vocab)
    # "songwriter" contains "writer" — don't tag a musician as a (screen)writer
    if "songwriter" in s and "screenplay" not in s and "co-writer" not in s:
        roles = [r for r in roles if r != "writer"]
    # a person can't hold an org role (and vice versa) — filter by entity kind
    allowed = PERSON_ROLES if kind == "person" else ORG_ROLES
    roles = [r for r in roles if r in allowed]
    if not roles and group_default:
        roles.append(group_default)
    return roles

def slug(name):
    return name.replace("/", "-").strip().replace(" ", "-")

def match_key(name):
    """Normalized key for finding an existing entity page under a variant spelling.
    Folds diacritics, lowercases, and unifies space/hyphen/underscore — but KEEPS
    meaningful punctuation like '+' (so 'AMC' and 'AMC+' stay distinct) and '&'.
    Catches the space-vs-hyphen + diacritic dup class without over-merging.
    (Guards the dup class where a later run would otherwise spawn 'Jane-Doe.md' beside an
    existing 'Jane Doe.md' — normalize-matching appends to the existing page instead.)"""
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = s.lower()
    s = re.sub(r"[\s_\-]+", " ", s).strip()
    return s

def resolve_entity_path(folder, name):
    """Path to write this entity's page to: the exact canonical hyphenated path if it
    exists; else an existing page under a normalized-variant spelling — flat
    (First-Last.md) OR active-contact folder (First-Last/First-Last.md) — append
    there, don't spawn a dup; else the canonical path (create new)."""
    canonical = os.path.join(folder, slug(name) + ".md")
    if os.path.exists(canonical):
        return canonical
    key = match_key(name)
    if os.path.isdir(folder):
        for f in os.listdir(folder):
            full = os.path.join(folder, f)
            # flat page: First-Last.md
            if f.endswith(".md") and f != "CLAUDE.md" and match_key(f[:-3]) == key:
                return full  # existing flat variant — append here
            # active-contact folder: First-Last/First-Last.md (the entity page lives inside)
            if os.path.isdir(full) and match_key(f) == key:
                inner = os.path.join(full, f + ".md")
                if os.path.exists(inner):
                    return inner  # existing folder-shaped page — append here
    return canonical  # no match — create at canonical hyphenated path

def parse_title_file(path):
    text = open(path, encoding="utf-8").read()
    # type from YAML
    m = re.search(r'^type:\s*(\S+)', text, re.M)
    typ = m.group(1).strip() if m else None
    # H1 title (display)
    m = re.search(r'^#\s+(.+)$', text, re.M)
    title = m.group(1).strip() if m else os.path.basename(path)[:-3]
    filename = os.path.basename(path)  # actual file (may differ from H1, e.g. stripped colon)
    # Who's Involved block
    block = text.split("## Who's Involved", 1)
    entries = []
    if len(block) > 1:
        body = block[1].split("\n## ", 1)[0]  # until next H2
        cur_kind, cur_default = "person", None
        for line in body.splitlines():
            line = line.rstrip()
            bold = re.match(r'^\*\*(.+?)\*\*\s*$', line.strip())
            if bold:  # group header like **Cast**
                cur_kind, cur_default = classify_group(bold.group(1))
                continue
            li = re.match(r'^-\s+\*\*(.+?)\*\*(.*)$', line.strip())
            if li:  # any bullet whose first bold span is the entity name
                name = li.group(1).strip()
                rest = li.group(2).strip()  # may be: "— suffix" / "(alias) — suffix" / ""
                parts = re.split(r'\s*(?:—|--|-)\s*', rest, maxsplit=1)
                suffix = parts[1].strip() if len(parts) == 2 else ""
                # strip a parenthetical alias on the name itself, e.g. Jean Giraud ("Moebius")
                name = re.sub(r'\s*\(.*?\)\s*$', '', name).strip()
                roles = role_vocab(cur_default, suffix, cur_kind)
                entries.append((cur_kind, name, suffix, roles))
    return typ, title, filename, entries

def yaml_roles(existing_text):  # reads the `category:` index (var names kept for brevity)
    m = re.search(r'^category:\s*\[(.*?)\]', existing_text, re.M)
    if not m:
        return []
    return [x.strip().strip('"').strip("'") for x in m.group(1).split(",") if x.strip()]

def fmt_roles(roles):
    return "[" + ",".join(f'"{r}"' for r in roles) + "]"

def propagate(title_path, stats):
    typ, title, filename, entries = parse_title_file(title_path)
    folder = TYPE_FOLDER.get(typ)
    if not folder:
        print(f"  ! skip (unknown type {typ}): {title_path}")
        return
    # merge duplicate names within this title (union roles, first suffix wins)
    merged = {}
    order = []
    for kind, name, suffix, roles in entries:
        key = (kind, name)
        if key not in merged:
            merged[key] = {"suffix": suffix, "roles": list(roles)}
            order.append(key)
        else:
            for r in roles:
                if r not in merged[key]["roles"]:
                    merged[key]["roles"].append(r)
            if not merged[key]["suffix"]:
                merged[key]["suffix"] = suffix
    for key in order:
        kind, name = key
        suffix = merged[key]["suffix"]
        roles = merged[key]["roles"]
        sub = "people" if kind == "person" else "organizations"
        epath = resolve_entity_path(os.path.join(LIB, sub), name)
        # backlink path is relative to where the entity page actually lives —
        # flat (../{type}/) vs active-contact folder (../../{type}/)
        # abspath both sides: relpath() resolves a relative `start` against the CWD, so an
        # absolute title_path (what an AI's tool call usually passes) produced ../../../../…
        # climbing to / and back — resolved on that one machine, leaked the full path.
        # realpath, not abspath: /tmp → /private/tmp on macOS, and any symlinked folder, would
        # otherwise leave the two sides disagreeing and reproduce the climb.
        rel = os.path.relpath(os.path.realpath(title_path), os.path.realpath(os.path.dirname(epath)))
        backlink = f"- [{title}]({url_escape(rel)})" + (f" — {suffix}" if suffix else "")
        if os.path.exists(epath):
            etext = open(epath, encoding="utf-8").read()
            changed = False
            # idempotent backlink — check BOTH spellings. We write the escaped form, so
            # comparing only the raw `rel` against a page that already holds the escaped
            # link would find nothing and append a duplicate.
            if url_escape(rel) not in etext and rel not in etext:
                # insert under "## In My Library"
                if "## In My Library" in etext:
                    parts = etext.split("## In My Library", 1)
                    after = parts[1]
                    # find end of the existing backlink list (first blank line or next ##)
                    lines = after.splitlines(keepends=True)
                    insert_at = 1  # right after the header line
                    i = 1
                    while i < len(lines) and (lines[i].startswith("- ") or lines[i].strip()==""):
                        if lines[i].startswith("- "):
                            insert_at = i + 1
                        i += 1
                    # newline guard: if the line we insert after lacks a trailing newline,
                    # "".join would concatenate the two list items onto one line.
                    if 0 <= insert_at - 1 < len(lines) and lines[insert_at - 1] and not lines[insert_at - 1].endswith("\n"):
                        lines[insert_at - 1] += "\n"
                    lines.insert(insert_at, backlink + "\n")
                    etext = parts[0] + "## In My Library" + "".join(lines)
                else:
                    etext = etext.rstrip() + f"\n\n## In My Library\n{backlink}\n"
                changed = True
                stats["appended"] += 1
            # merge roles
            cur = yaml_roles(etext)
            newroles = cur + [r for r in roles if r not in cur]
            if newroles != cur:
                if re.search(r'^category:.*$', etext, re.M):
                    etext = re.sub(r'^category:.*$', f"category: {fmt_roles(newroles)}", etext, count=1, flags=re.M)
                else:
                    # add category: after type: line
                    etext = re.sub(r'^(type:.*)$', r'\1\ncategory: ' + fmt_roles(newroles), etext, count=1, flags=re.M)
                changed = True
            if changed:
                open(epath, "w", encoding="utf-8").write(etext)
        else:
            etype = "person" if kind == "person" else "organization"
            rolesline = f"category: {fmt_roles(roles)}\n" if roles else ""
            why = "" if kind == "person" else "\n## Why I'm Watching\n*(added later, when interest is real)*\n"
            content = (
                f"---\nname: {name}\ntype: {etype}\ndate_added: {datetime.date.today().isoformat()}\n{rolesline}---\n\n"
                f"# {name}\n\n## In My Library\n{backlink}\n{why}"
            )
            os.makedirs(os.path.dirname(epath), exist_ok=True)  # a fresh system has no people/ or organizations/ yet
            open(epath, "w", encoding="utf-8").write(content)
            stats["created"] += 1

def main():
    stats = {"created": 0, "appended": 0}
    for p in sys.argv[1:]:
        print(f"· {p}")
        propagate(p, stats)
    print(f"\nDone. Entity pages created: {stats['created']}, backlinks appended to existing: {stats['appended']}")

if __name__ == "__main__":
    main()
