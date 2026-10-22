# Operating contract

Read this file at the start of every session, before doing anything else.

On the first read, if the two sections below are still empty, ask the owner
two questions, one at a time: what this base is for, and what it is NOT for.
Write each answer in the owner's words. "Not decided yet" is a fine answer;
write that down as an Open line in `state.md` and ask again after five
sources. Ask nothing else first.

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
   owner's OK (rule 3).
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
   source, this plain summary is the teach-back (rule 9).

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
