#!/usr/bin/env python3
"""
entity-backscan.py — when an entity enters the graph (a new people/ or organizations/
page is created), scan existing library titles + content for places that MENTION that
entity but don't credit them — surfacing candidate connections to wire by hand.

The pattern: an entity that already has a page (from one title) is named in another
title's cast/credits prose without being credited there. The high-signal filter is that the
entity ALREADY has a page — it has earned graph-presence (the codified lazy-cameo rule:
billed cast captured, the rest lazy "until earned"). This script finds where an earned
entity is mentioned-but-unwired.

NOT an auto-wirer — output is a REVIEW LIST. A text match can't tell a real cameo from a
cited-reference, a deliberately-scoped-out credit (e.g. "not billed principals"), or a
character-name collision (an "Actor — Character" line where the character happens to
share a real person's name). The script filters the obvious noise; a human makes the
call on each remaining candidate and wires the real ones (add to YAML + Who's-Involved,
then re-run propagate-entities.py / propagate-content-entities.py).

THE PER-ADD TRIGGER (why this lives with /add): run it on the names a propagation run
reports as `created`. New entity → backscan its name against everything we already hold.
One name at a time = almost no noise; the full-library sweep (all entities) is the same
logic fired occasionally (e.g. from /audit).

Usage:
  python3 Core/skills/add/entity-backscan.py "Entity Name" ...
Run from your OS root. Pass the entity name(s) just added.
"""
import os, re, sys, importlib.util

# Real casing from disk (see propagate-entities.py: a guessed casing broke backlink paths on Mac)
LIB = next((d for d in os.listdir(".") if d.lower() == "library" and os.path.isdir(d)), "library")
# (Without the fallback this is lowercase-only: fine on a case-insensitive Mac disk,
# but on Linux/WSL every SCAN_DIR below misses, the loop finds nothing, and the script
# reports "Graph is already wired" — a clean negative about a library it never opened.)

# Where an entity could be MENTIONED (title hubs + flat content with bodies/prose).
# Discovered, not hardcoded: your Library is whatever folders you actually made, so scan
# them all and skip only the ones that aren't prose. (A fixed list would silently miss
# every folder you named yourself — and Library/CLAUDE.md explicitly invites you to.)
SKIP_DIRS = {
    "people",       # entity pages themselves — that's the target, not the haystack
    "organizations",
    "_tags.md",
}
SCAN_DIRS = sorted(
    d for d in os.listdir(LIB)
    if os.path.isdir(os.path.join(LIB, d))
    and d not in SKIP_DIRS
    and not d.startswith(".")
) if os.path.isdir(LIB) else []

# reuse the hardened normalize-match from the propagation script (variant-spelling-safe
# credit check — so a YAML credit counts even across spelling variants of its page name)
_pe = os.path.join(os.path.dirname(os.path.abspath(__file__)), "propagate-entities.py")
_spec = importlib.util.spec_from_file_location("propagate_entities", _pe)
pe = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pe)


def yaml_names(text):
    """Names already credited in this file's people: / organizations: YAML (inline or block)."""
    names = set()
    for key in ("people", "organizations"):
        m = re.search(r'^' + key + r':\s*\[(.*?)\]', text, re.M | re.S)
        if m:
            names |= {x.strip().strip('"').strip("'") for x in m.group(1).split(",") if x.strip()}
            continue
        lines = text.splitlines()
        for i, l in enumerate(lines):
            if re.match(r'^' + key + r':\s*$', l):
                for j in range(i + 1, len(lines)):
                    mm = re.match(r'^\s*-\s+(.*)$', lines[j])
                    if mm:
                        names.add(mm.group(1).strip().strip('"').strip("'"))
                    elif lines[j].strip() == "":
                        continue
                    else:
                        break
                break
    return names


def is_character_line(line, name):
    """True if the name is the RHS of an 'Actor — Character' credit (a role, not a credit) —
    e.g. '- **Some Actor** — Character Name'. Kills the character-name-collision false positive."""
    return bool(re.search(r'[—–\-]\s*' + re.escape(name) + r'\s*$', line.strip()))


def backscan(name, hits):
    multi = " " in name
    nkey = pe.match_key(name)
    word = re.compile(r'(?<![\w])' + re.escape(name) + r'(?![\w])')
    for d in SCAN_DIRS:
        folder = os.path.join(LIB, d)
        if not os.path.isdir(folder):
            continue
        for f in os.listdir(folder):
            if not f.endswith(".md") or f == "CLAUDE.md":
                continue
            text = open(os.path.join(folder, f), encoding="utf-8").read()
            # skip files that already credit this entity (normalize-match → variant-spelling-safe)
            if any(pe.match_key(c) == nkey for c in yaml_names(text)):
                continue
            for line in text.splitlines():
                if word.search(line):
                    if is_character_line(line, name):
                        continue  # it's a character name, not this entity
                    sec = "cast/credits" if re.search(
                        r'cast|cameo|involved|voice|plays|compos|direct|writ|produc|member|label|score',
                        line, re.I) else "prose"
                    flag = "" if multi else "  [single-token name — verify (common-word risk)]"
                    hits.append((d, f[:-3], name, sec, line.strip()[:100], flag))
                    break


def main():
    if len(sys.argv) < 2:
        print('usage: entity-backscan.py "Name" ["Name" ...]   (pass the entity names just added)')
        return
    hits = []
    for name in sys.argv[1:]:
        backscan(name, hits)
    if not hits:
        print("No mention-but-uncredited candidates. Graph is already wired for these names.")
        return
    print("Candidate connections — entity has a page AND is mentioned in a title that doesn't credit it:\n")
    for d, title, name, sec, line, flag in sorted(hits):
        print(f"  [{sec:12}] {d}/{title}  ←  {name}{flag}")
        print(f"               …{line}")
    print(f"\n{len(hits)} candidate(s) to REVIEW. Wire the real cameos/credits (add to YAML + Who's-Involved,")
    print("then re-run propagate-entities.py / propagate-content-entities.py). Skip cited-references,")
    print("deliberate scope-outs ('not billed principals'), and any character-name matches that slipped through.")


if __name__ == "__main__":
    main()
