#!/usr/bin/env python3
"""Generate library/_tags.md — the canonical tag vocabulary for /add to reuse.
Run from your system root: python3 Core/skills/add/build-tag-vocab.py"""
import os, re, glob, collections
LIB = next((d for d in os.listdir(".") if d.lower() == "library" and os.path.isdir(d)), "library")  # real casing from disk
tags=collections.Counter()
for f in glob.glob(f"{LIB}/**/*.md", recursive=True):
    # organizations/ are catalog items too, and carry reusable
    # modifier tags (city / cuisine / tool-domain) — include them. people/ still excluded:
    # their tags are a CRM-relationship vocabulary (student / cold-outreach / cohort), not
    # content topics, so they'd be noise in the /add reuse-reference. repos/ = cloned code.
    if any(x in f for x in ("/people/","/repos/")): continue
    t=open(f,encoding="utf-8",errors="replace").read()
    if not t.startswith("---"): continue
    end=t.find("\n---",3); fm=t[:end] if end>0 else ""
    mi=re.search(r'^tags:[ \t]*\[(.*?)\][ \t]*$', fm, re.M)
    mb=re.search(r'^tags:[ \t]*\n((?:[ \t]*-[ \t].*\n?)+)', fm, re.M)
    if mi: items=[x.strip().strip('"').strip("'") for x in mi.group(1).split(",") if x.strip()]
    elif mb: items=[re.sub(r'^[ \t]*-[ \t]*','',l).strip().strip('"').strip("'") for l in mb.group(1).rstrip().split("\n")]
    else: continue
    for x in items:
        if x: tags[x]+=1
lines=[f"- `{t}` ({c})" for t,c in sorted(tags.items(), key=lambda x:(-x[1],x[0]))]
body=("# Library Tag Vocabulary\n\n"
      f"**{len(tags)} canonical tags** — generated, regenerate with `python3 Core/skills/add/build-tag-vocab.py`.\n\n"
      "**Reuse-reference for `/add`:** before minting a new tag, skim this list and reuse an existing one. "
      "Lowercase-kebab-case only. Mint new *only* when nothing here fits — this keeps your tags from sprawling "
      "into near-duplicates that fragment the facet.\n\n" + "\n".join(lines) + "\n")
open(f"{LIB}/_tags.md","w",encoding="utf-8").write(body)
print(f"wrote {LIB}/_tags.md ({len(tags)} tags)")
