#!/usr/bin/env python3
"""
dup-check.py — the /wrap-end verification gate for the forward-state trio.

ALIVE.md / PULLING.md / THREADS.md are meant to be mutually exclusive: an actionable
belongs on exactly ONE surface. This flags actionables that look like they're tracked in
two+ of them — the duplication the /wrap Step-1 crisp-action gate is supposed to prevent,
caught after the fact.

DETECTION ONLY — flags candidate dup-pairs for a human to consolidate; never edits.

It is a **heuristic flagger, not a clean total gate.** "Same actionable" is a judgment, not a
deterministic boundary, so it compares word overlap and will both miss real duplicates worded
differently and flag pairs that merely share a topic. A clean run is weak evidence, not proof.
The judgment stays with you; the script only saves you the scanning.

Reading the flags by pair-type:
  ALIVE ↔ PULLING  — likely a true duplicate. Both are forward surfaces and should be
                     mutually exclusive; consolidate to one.
  either ↔ THREADS — usually means the work finished. A forward item overlapping its own
                     record is a tombstone; prune the forward copy.

On a brand-new system it will report that it examined 0 items — that is not a pass, it just
means nothing has been routed to the three files yet. Read the items-examined count next to
the result, always. It starts doing real work once you've wrapped a few sessions.

Usage:  dup-check.py [--root PATH] [--recent N] [--min-shared K] [--min-jaccard F]
Exit 0 = no dup candidates · 1 = candidates surfaced · 2 = scanned 0 files (suspect: bad root).
"""
import sys, re, argparse, itertools
from pathlib import Path


def repo_root():
    """Self-locate the root by walking up to the AGENTS.md landmark — never trust the
    caller's cwd. A script that silently scans the wrong place exits 0 having done nothing,
    which reads exactly like success."""
    p = Path(__file__).resolve()
    for d in (p, *p.parents):
        if (d / "AGENTS.md").exists():
            return d
    return Path.cwd()  # last resort; the empty-guard below will catch a bad landing

# topic words drown the signal (this week every surface says "rules / codification / retrieval");
# distinctive-token + high-proportion overlap is what marks the *same actionable*, not the same topic.
STOP = set("""a an the this that these those and or but so if when while then there here it he she
they we you i my our your his her their its is are was were be been being do does did for to of in
on at by with as from up out no not now like just ok okay yeah dude because per via into onto over
under about after before during one two get got make made go going need needs want wants will would
can should could may might more most less also still yet only even than them too etc what which who
how why where new old next last each both per use used using thing things stuff way ways done""".split())


def items(text, recent=None):
    """Extract actionable-ish lines (bullets / checkboxes), optionally only the first `recent` lines
    (THREADS is most-recent-first and ALIVE/PULLING keep live items at the top, so the head is what matters)."""
    lines = text.splitlines()
    if recent:
        lines = lines[:recent]
    out = []
    for ln in lines:
        s = ln.strip()
        if re.match(r"^[-*]\s|^\d+\.\s", s):
            body = re.sub(r"^[-*]\s*(\[.\]\s*)?", "", s)
            body = re.sub(r"^\d+\.\s*", "", body)
            body = re.sub(r"[*_`>#\[\]()]", " ", body)
            if len(body.split()) >= 4:
                out.append((s, body))
    return out


def sig(body):
    return {t for t in re.sub(r"[^a-z0-9 ]", " ", body.lower()).split()
            if t not in STOP and len(t) >= 4}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None,
                    help="repo root (default: self-locate via AGENTS.md walk-up, cwd-independent)")
    ap.add_argument("--recent", type=int, default=180,
                    help="only the first N lines of each file (the live head: THREADS is most-recent-first, ALIVE/PULLING keep live items on top)")
    # 3, not 5: a short bullet ("Finish the onboarding doc draft review") is 4-7 words
    # but only ~2-4 distinctive tokens (4+ letters, not a stopword), so a floor of 5
    # silently blocks most real duplicates in a young system.
    # Measured on a 1,022-item mature corpus: 5 and 3 flag identically (dense prose is
    # gated by jaccard, not the floor), so the lower floor costs nothing and catches more.
    ap.add_argument("--min-shared", type=int, default=3)
    ap.add_argument("--min-jaccard", type=float, default=0.45)
    a = ap.parse_args()
    root = Path(a.root) if a.root else repo_root()
    catalog = {}
    for f in ("ALIVE.md", "PULLING.md", "THREADS.md"):
        p = root / f
        if p.exists():
            catalog[f] = [(raw, sig(body)) for raw, body in items(p.read_text(errors="ignore"), a.recent)]

    # Empty-guard: a gate that scanned nothing must NOT report clean. "Total over the empty
    # set" is the most dangerous false green there is — it looks identical to real success.
    if not catalog:
        print(f"\n⚠ dup-check scanned 0 of 3 trio files under {root} — is the root right?\n"
              f"  (expected ALIVE.md / PULLING.md / THREADS.md; none found)\n", file=sys.stderr)
        sys.exit(2)

    flags = []
    for fa, fb in itertools.combinations(catalog, 2):
        for ra, sa in catalog[fa]:
            if len(sa) < a.min_shared:
                continue
            for rb, sb in catalog[fb]:
                shared = sa & sb
                if len(shared) < a.min_shared:
                    continue
                jac = len(shared) / len(sa | sb)
                if jac >= a.min_jaccard:          # same actionable, not just same topic
                    flags.append((fa, fb, jac, sorted(shared)[:8], ra, rb))

    # Declare coverage next to the verdict. A green over 0 examined items is not a pass,
    # and without this line it looks exactly like one.
    n_items = sum(len(v) for v in catalog.values())
    print(f"\n── dup-check ── ALIVE ↔ PULLING ↔ THREADS  "
          f"({len(catalog)}/3 files · {n_items} items examined · first {a.recent} lines each · "
          f"≥{a.min_shared} shared tokens · Jaccard ≥{a.min_jaccard})\n")
    if n_items == 0:
        print("⚠ nothing to check — found the files but extracted 0 items.\n"
              "  Normal on a new system (nothing routed yet). NOT a pass.\n", file=sys.stderr)
        sys.exit(0)
    if not flags:
        print("✓ clean — no actionable appears tracked in two surfaces\n")
        sys.exit(0)
    for fa, fb, jac, shared, ra, rb in sorted(flags, key=lambda x: -x[2]):
        print(f"⚑ {fa} ↔ {fb}  (jaccard {jac:.2f} · shared: {', '.join(shared)})")
        print(f"    {fa}: {ra[:150]}")
        print(f"    {fb}: {rb[:150]}\n")
    print(f"⚑ {len(flags)} candidate dup-pair(s) — consolidate each to ONE surface\n")
    sys.exit(1)


if __name__ == "__main__":
    main()
