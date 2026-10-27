#!/usr/bin/env python3
"""Emit a seed Soulvant: the folder skeleton, the operating contract, and the
starter pages a new owner needs on day one.

The seed carries portable primitives only. It deliberately leaves out the
configuration choices that belong to one owner rather than to the pattern:
typography rules, prose watchlists, decay scoring, a specific ledger schema,
a named agent roster. A new owner should set their own equivalents, or none.

Usage:
    py -3 scripts/soulvant_seed.py --out "C:/path/Soulvant Seed"
    py -3 scripts/soulvant_seed.py --out ./seed --zip
    py -3 scripts/soulvant_seed.py --out ./seed --owner "Ada Lovelace"

Add --schematic to embed a generated schematic of THIS vault as an example
of what the pattern looks like once it has been running for a while.
"""

import argparse
import datetime
import os
import shutil
import sys

FOLDERS = [
    ("00 - MOCs", "Synthesis pages. One per topic you keep returning to."),
    ("10 - Notes", "Atomic notes. One idea per page, every claim cited."),
    ("20 - Sources", "Your raw material. Never rewritten, by anyone."),
    ("20 - Sources/Conversations", "Transcripts and chat logs you own a copy of."),
    ("20 - Sources/Clippings", "Articles, papers, transcripts saved from the web."),
    ("20 - Sources/Drafts", "Your own long-form writing, versioned."),
    ("30 - Projects", "What you are building or running."),
    ("40 - People", "Recurring people, so context about them accumulates."),
    ("80 - Maintenance", "The assistant's own working artifacts."),
    ("90 - Inbox", "Dropped material waiting to be processed."),
]

CONTRACT = """# Operating contract

Read this file at the start of every session, before doing anything else.

On the first read, if the two sections below are still empty, process the
first file in `90 - Inbox/` before anything else (see Process one source).
Once it is filed, ask the owner two questions, one at a time: what this base
is for, and what it is NOT for. If the Inbox is empty, ask them first.
Write each answer in the owner's words. "Not decided yet" is a fine answer;
write that down as an Open line in `state.md` and ask again after five
sources.

## What this base is for

<!-- Owner: replace this. One or two sentences. What decisions or work does
this base exist to support? Be specific enough that it excludes things. -->

## What this base is NOT for

<!-- Owner: replace this too. This section is the one that keeps the base
useful. Without it, everything lands here and nothing is findable. -->

## Who does what

The owner decides what is worth keeping and what it means. The assistant does
the reading, summarizing, filing, cross-linking, and upkeep. That division is
the whole idea: an ordinary notebook falls out of date because maintaining it
is a chore, and this one stays current because the chore costs almost nothing.

## Layout

```
00 - MOCs/      synthesis pages, one per topic
10 - Notes/     atomic notes, one idea each
20 - Sources/   raw material, immutable
30 - Projects/  what is being built
40 - People/    recurring people
80 - Maintenance/  the assistant's working artifacts
90 - Inbox/     unprocessed material
index.md        catalog: every page, one line each
log.md          append-only record of what changed and why
state.md        what is open, in flight, and decided
```

## Rules the assistant follows

1. **Sources are never rewritten.** Anything under `20 - Sources/` is
   evidence. The assistant may add a new source file and may correct
   administrative frontmatter, but the body is the owner's material. If it
   needs a correction, raise it; do not silently edit it.

2. **Every claim cites a source.** An atomic note without a `## Sources`
   section is not finished. A claim that cannot point at where it came from
   does not belong in the base.

3. **Say what you found before writing.** After reading a new source, tell the
   owner what it says and what you intend to write. A misread caught here
   costs one sentence; caught later it costs a rewrite of everything
   downstream.

4. **Flag contradictions, never resolve them silently.** When new material
   disagrees with something already filed, surface both and let the owner
   decide. Averaging two positions into one destroys the disagreement, which
   is usually the most valuable thing in the base.

5. **Keep the voice of an idea distinct from the owner's.** When a source
   argues something, the page records that this source argues it, not that
   the owner believes it. Ideas arrive from inboxes, transcripts, group
   chats, and social feeds, and some of them are being examined rather than
   held. Without provenance there is no way to tell those apart later.

6. **Every page links up.** An atomic note links to at least one synthesis
   page. Nothing is an orphan.

7. **Update the catalog and the log every time.** A new or removed page means
   `index.md` changes. Every session that changed something appends to
   `log.md` under a dated heading, naming the pages touched.

8. **Propose, do not overwrite meaning.** Structural cleanup is the
   assistant's to do. Changing what a page claims is the owner's call.

9. **Teach it back.** After a real change, walk the owner through what
   changed and why, so the understanding stays theirs rather than something
   they approved.

## Frontmatter

Every page the assistant writes carries at least:

```yaml
---
type: moc | note | person | source | project
description: one line, mirrored into index.md
updated: YYYY-MM-DD
---
```

## Process one source

Take one file from `90 - Inbox/` at a time.

1. Read it. Say what you found and what you will write, then wait for the
   owner's OK (rule 3). If the owner only wants to read or talk it over, do
   that and file nothing: leave the file in `90 - Inbox/` until they say to
   file it.
2. Move it into `20 - Sources/`: `Clippings/` for articles and papers,
   `Conversations/` for chats and transcripts, `Drafts/` for the owner's own
   writing. Name it `YYYY-MM-DD - Author - Title.md`, using the date it was
   written, or the date saved if unknown. Author is the owner's name if known,
   else "Me", for the owner's own writing. Leave the body as it is and add
   frontmatter above it:

```yaml
---
type: source
description: Article on sourdough starter ratios
updated: 2026-10-21
---
```

   A source may also carry `author:` and `date:`. Add no other keys.

3. Write one atomic note per idea in `10 - Notes/`. The file name is the claim
   as a sentence, without colons. Link it up to a synthesis page, and cite
   the source:

```markdown
---
type: note
description: A starter fed equal parts by weight rises on a steady schedule
updated: 2026-10-21
---
A starter fed equal parts flour, water and old starter by weight rises on a
steady schedule. Part of [[MOC - Sourdough]].

## Sources
- [[2026-10-20 - Jane Baker - Starter basics]]: says an equal-parts feeding
  peaks in 4 to 6 hours.
```

4. If no synthesis page covers the topic, make one in `00 - MOCs/` named
   `MOC - Topic.md`: a heading, then one line per note.

```markdown
# MOC - Sourdough
- [[A starter fed equal parts by weight rises on a steady schedule]]
```

5. Add each new page to `index.md`, append to `log.md`, and update
   `state.md` if anything is open or decided. Log the `CLAUDE.md` setup edit as
   its own line.
6. Tell the owner what was filed, then ask about the next file. For a first
   source, this plain summary is the teach-back (rule 9). If the owner says
   to do the rest, list what each remaining file holds, wait for one OK for
   the list, then file them one at a time.

The `README.md` in each folder, including `90 - Inbox/`, is a label, not
material. Leave it alone. When you edit a file, keep its existing line
endings.

## The state page

`state.md` holds what is open, in flight, and decided, in one place rather
than scattered across lists. The assistant maintains it; the owner reads it.

It carries a priority order, and **the owner can change that order.** The
useful ordering differs by person: research-shaped work wants open questions
and contradictions surfaced first, action-shaped work wants the next move.
The owner sets it after the first week; leave it blank until then. Retune it
once the base has a few weeks of material in it.

Ask for a rundown any time and the assistant reads that page back, ordered.

## Sharing

Most of the base stays private. When the owner chooses, the assistant can
prepare a slice to send someone: the pages, the sources behind them, and a
catalog, as plain Markdown that drops into any other base. The owner reviews
it before it leaves. Nothing is exported by default.
"""

AGENTS_MD = """# AGENTS.md

This base follows the Soulvant / LLM-wiki pattern. The operating contract is
in `CLAUDE.md` at the root of this base. Read it first, whatever toolchain
you are.

The contract is deliberately harness-agnostic. It names what the base is for,
who decides what, which zones are protected, and the rules for writing into
it. Nothing in it depends on a particular model, vendor, or CLI.
"""

INDEX = """# Index

Updated: {date}

The catalog. Every page in this base appears here exactly once, with a
one-line description mirrored from the page's own `description:` field.

## MOCs

<!-- - [[MOC - Topic]] - one-line summary -->

## Atomic notes

<!-- - [[A claim stated as a sentence]] - one-line summary -->

## Sources

<!-- - [[2026-01-01 - Author - Title]] - what it is -->

## People

<!-- - [[First Last]] - role or relationship -->

## Projects

<!-- - [[Project name]] - one-line status -->
"""

LOG = """# Log

Append-only. Never edit an existing entry; if something was wrong, append a
correction that references it.

Every entry starts with a dated heading so the file stays greppable:

    ## [YYYY-MM-DD] <operation> | <one-line description>

Operations: ingest, query, research, lint, brief, learn, note.

An entry that changed pages names those pages, so the base can tell later
which material is in use and which has gone quiet.

## [{date}] note | Base created from a Soulvant seed

- Folder skeleton, operating contract, index, log, and state page created.
- Owner has not yet filled in the purpose and out-of-scope sections of the
  contract. The assistant asks for them after the first source is filed.
"""

STATE = """---
type: state
updated: {date}
---
# State

What is open, in flight, and decided. One place, maintained by the assistant,
read by the owner.

## Priority order

<!-- Owner: how should this page be ordered when it is read back to you?
Two shapes that work, pick one and change it later:

  research-shaped: open questions first, then contradictions, then sources
                   waiting to be processed, then everything else
  action-shaped:   what is next, then what is blocked and on whom, then
                   what is waiting on someone else, then everything else
-->

## Open

<!-- One line per live thread: what it is, what the next action is, when it
was last touched, and who it is blocked on if anyone. -->

## Decided

<!-- Decisions worth not relitigating, with the date and the reasoning. -->

## Open questions

<!-- Questions the base is carrying but has not answered. -->
"""

START_HERE = """# Start here

This is a seed Soulvant: an empty personal knowledge base that an AI
assistant maintains for you.

## The idea

A model is general knowledge with nothing personal in it. Your assistant's
session memory dies when the session does. Your raw files are long-term
memory but nothing has been made of them yet. This base is the layer in
between: durable, synthesized at the moment material comes in, and cited
back down to where each claim came from.

How an agent gets information and stores it is what gives it agency.
Otherwise it is a general model with a very confused memory.

## Your first day

1. **Put three or four sources you already care about in `90 - Inbox/`.**
   An article, a transcript, a chapter, something you wrote.
2. **Ask the assistant to process one of them.** Watch it tell you what it
   found before it writes anything. Correct it if it misread. If you only
   want to talk a file over, say so and it files nothing. Then look at the
   pages it produced and the catalog entry it added.
3. **Answer two questions.** After the first file, your assistant asks what
   this base is for and what it is not for, and writes your answers in. A
   sentence each is enough, and "not decided yet" is allowed. The second
   answer matters more than the first. Then it asks about the other files.
4. **Ask it a question** that the source you just added should be able to
   answer, and check that the answer cites it.
5. **Stop there.** Do not set up git, sync, or anything else on day one. The
   first loop is the proof. The rest can wait until you want it.

## What you need

- **An AI assistant** that can read and write files in this folder.
- **A Markdown editor.** Obsidian is free and shows you the shape of what you
  know through its graph view. Any editor works; these are plain text files.
- **git**, eventually, for version history and backup. Not on day one.

## What this asks of you

You decide what is worth keeping and what it means. The assistant does the
reading, filing, and cross-linking that nobody sustains alone. It rewards a
focused collection you return to over time far more than a place where
everything gets dumped.
"""


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def build(out, owner, date, schematic_from=None):
    if os.path.exists(out) and os.listdir(out):
        sys.exit("refusing to write into a non-empty directory: %s" % out)

    for folder, blurb in FOLDERS:
        d = os.path.join(out, folder)
        os.makedirs(d, exist_ok=True)
        write(os.path.join(d, "README.md"), "# %s\n\n%s\n" % (folder, blurb))

    contract = CONTRACT
    if owner:
        contract = contract.replace(
            "# Operating contract",
            "# Operating contract\n\nOwner: %s" % owner)

    write(os.path.join(out, "CLAUDE.md"), contract)
    write(os.path.join(out, "AGENTS.md"), AGENTS_MD)
    write(os.path.join(out, "index.md"), INDEX.format(date=date))
    write(os.path.join(out, "log.md"), LOG.format(date=date))
    write(os.path.join(out, "state.md"), STATE.format(date=date))
    write(os.path.join(out, "START HERE.md"), START_HERE)

    if schematic_from:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import soulvant_schematic as sch
        text = sch.render(schematic_from, None, 72, title="an example, after 3 months")
        write(os.path.join(out, "80 - Maintenance", "Example schematic.md"),
              "# What this looks like later\n\n"
              "An example from another working Soulvant, not yours. It is not filed\n"
              "material and not a layout to copy. Yours starts empty and grows into a\n"
              "shape like this one.\n\n"
              "```\n" + text + "\n```\n")

    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, help="directory to create the seed in")
    ap.add_argument("--owner", default=None)
    ap.add_argument("--zip", action="store_true", help="also produce a .zip beside it")
    ap.add_argument("--schematic", action="store_true",
                    help="embed a schematic of this vault as an example")
    ap.add_argument("--vault", default=os.path.join(os.path.dirname(__file__), ".."))
    ap.add_argument("--date", default=None)
    args = ap.parse_args()

    date = args.date or datetime.date.today().isoformat()
    out = os.path.abspath(args.out)
    build(out, args.owner, date, args.vault if args.schematic else None)

    files = sum(len(f) for _, _, f in os.walk(out))
    print("seed written to %s (%d files)" % (out, files))

    if args.zip:
        archive = shutil.make_archive(out, "zip", root_dir=os.path.dirname(out),
                                      base_dir=os.path.basename(out))
        size = os.path.getsize(archive) / 1024.0
        print("zipped to %s (%.1f KB)" % (archive, size))


if __name__ == "__main__":
    main()
