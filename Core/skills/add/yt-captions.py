#!/usr/bin/env python3
"""
yt-captions.py — collapse a YouTube auto-caption VTT into usable text.

YouTube's auto-generated VTTs are ROLLING: each cue repeats the previous line
plus new words, and the new words carry inline per-word timing tags
(`<00:00:03.480><c>word</c>`). A naive tag-strip yields every line ~3x. This
keeps only the new-text lines, strips tags, and drops consecutive duplicates.

Two output modes:
  --prose     paragraphs (~8 cues each). For reading / a plain capture.
  --stamped   `N<TAB>[H:MM:SS]<TAB>text` per cue. Use this when you'll want
              timestamps later — to place the creator's chapter markers at their
              real positions, or to hand bounded cue ranges to a sub-agent.

Usage:
  python3 Core/skills/add/yt-captions.py IN.vtt OUT.txt [--prose|--stamped] [--per N]

Upstream (get the VTT + the metadata):
  yt-dlp --no-update --skip-download --write-auto-subs --write-subs \
    --sub-langs "en.*" --sub-format vtt -o "%(id)s.%(ext)s" URL
  yt-dlp --no-update --skip-download --print "%(description)s" URL   # chapters + real quotes

Note: en.vtt and en-orig.vtt are usually byte-identical; either works.

⚠️ AUTO-caption output is NOT quote-grade — no speaker labels, no punctuation, and
proper nouns arrive mangled. Treat the video as ground truth; fix a garbled name
when you spot one (what the captioner heard wrong, never what the speaker said).

⚡ But `--write-subs` also pulls MANUAL/broadcast caption tracks, and those are a
different quality class: real punctuation, real capitalisation, and `>>` speaker-CHANGE
markers (change only — still no names). Anything originally broadcast on TV likely has
them. Head the .txt and look for sentence case and terminal punctuation. If it reads
like a script, it roughly is one.
"""
import html
import re
import sys


def parse(path):
    """VTT -> [(timestamp, text)] with rolling duplicates removed.

    Each rolling cue block is `carry-over line` + `new-content line`. The new
    content is USUALLY tagged with per-word timings — but not always: a word can
    settle as plain text (a block reading just `confused`). So take the LAST line
    of each block regardless of tagging, and drop it only if it repeats what was
    already emitted.

    ⚠️ Do NOT go back to `if "<" not in ln: continue`. That treated *every*
    untagged line as a carry-over repeat, which silently deleted any new content
    that arrived untagged — 151 fragments on a single 1h53m episode, each one a
    word or clause vanishing mid-sentence. It failed invisibly: the loss never
    entered the "raw" stream, so a completeness check compared lossy against
    lossy and passed green, and the gaps got reported as "the captions dropped
    words" — a defect nearly recorded as a fact about YouTube.
    """
    rows, ts = [], None
    blocks, cur = [], []
    for ln in open(path, encoding="utf-8").read().splitlines():
        if ln.startswith(("WEBVTT", "Kind:", "Language:")):
            continue
        m = re.match(r"(\d{2}):(\d{2}):(\d{2})\.\d+\s+-->", ln)
        if m:
            if cur:
                blocks.append(cur)
            h, mi, s = (int(x) for x in m.groups())
            cur = [(f"{h}:{mi:02d}:{s:02d}" if h else f"{mi}:{s:02d}")]
            continue
        if ln.strip() and cur:
            cur.append(ln)
    if cur:
        blocks.append(cur)

    for blk in blocks:
        ts, lines = blk[0], blk[1:]
        if not lines:
            continue
        # Strip timing tags FIRST, then unescape entities. Order is load-bearing:
        # unescaping first would turn a literal `&lt;c&gt;` into `<c>` and the
        # tag-strip would then delete it as markup. Broadcast caption tracks carry
        # `&gt;&gt;` speaker-change markers and `&amp;`/`&#39;` in dialogue; they
        # were passing through raw into every capture before this.
        txt = html.unescape(re.sub(r"<[^>]+>", "", lines[-1])).strip()
        if txt and not (rows and rows[-1][1] == txt):
            rows.append((ts, txt))
    return rows


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if len(args) < 2:
        sys.exit(__doc__.strip())
    src, out = args[0], args[1]
    per = 8
    if "--per" in sys.argv:
        per = int(sys.argv[sys.argv.index("--per") + 1])

    rows = parse(src)
    if not rows:
        sys.exit(f"no caption cues found in {src} — is it a real auto-caption VTT?")

    if "--stamped" in flags:
        body = "\n".join(f"{i}\t[{ts}]\t{t}" for i, (ts, t) in enumerate(rows, 1))
        note = f"{len(rows)} cues (stamped)"
    else:
        texts = [t for _, t in rows]
        paras = [" ".join(texts[i:i + per]) for i in range(0, len(texts), per)]
        body = "\n\n".join(paras)
        note = f"{len(rows)} cues -> {len(paras)} paragraphs"

    open(out, "w", encoding="utf-8").write(body + "\n")
    print(f"{note}, {sum(len(t.split()) for _, t in rows)} words -> {out}")


if __name__ == "__main__":
    main()
