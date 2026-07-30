# Operating contract

Read this file at the start of every session, before doing anything else.

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

## The state page

`state.md` holds what is open, in flight, and decided, in one place rather
than scattered across lists. The assistant maintains it; the owner reads it.

It carries a priority order, and **the owner can change that order.** The
useful ordering differs by person: research-shaped work wants open questions
and contradictions surfaced first, action-shaped work wants the next move.
Pick one, then retune it once the base has a few weeks of material in it.

Ask for a rundown any time and the assistant reads that page back, ordered.

## Sharing

Most of the base stays private. When the owner chooses, the assistant can
prepare a slice to send someone: the pages, the sources behind them, and a
catalog, as plain Markdown that drops into any other base. The owner reviews
it before it leaves. Nothing is exported by default.
