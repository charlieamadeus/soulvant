# Soulvant

*Intelligence for Cyborgs.*

A personal knowledge base that an AI assistant keeps current. You decide what
is worth keeping and what it means. It does the reading, filing, cross-linking,
and upkeep that nobody sustains alone.

**[Read the explainer first.](https://charlieamadeus.github.io/soulvant/)**
It is one page and it is the whole idea in plain language.

---

## Why this exists

A model is general knowledge with nothing personal in it. Your chat session
forgets everything when it closes. Your files are long-term memory that nothing
has been made of yet. Soulvant is the layer in between: durable, synthesized
when material comes in, and cited back down to where every claim came from.

How an agent gets information and stores it is what gives it agency. Otherwise
it is a general model with a very confused memory.

## Start one

You do not need Python, a terminal, or any of the tooling in this repo.

1. **Download this repo** (green `Code` button, then `Download ZIP`) and unzip
   it, or clone it if that is your habit.
2. **Take the `seed/` folder** out and rename it whatever your base should be
   called. That folder is your Soulvant. Everything else here is optional.
3. **Open it in [Obsidian](https://obsidian.md)** as a vault. Obsidian is free.
   Any Markdown editor works; these are plain text files.
4. **Point an AI assistant at that folder.** One that can read and write files
   in it. Claude Code, Codex, or anything comparable.
5. **Open `START HERE.md`** and do what it says. The first thing is filling in
   two blank sections of the operating contract with your assistant, out loud:
   what this base is for, and what it is not for. The second one matters more.

Then add three or four sources you already care about and ask your assistant to
process one. Watch it tell you what it found before it writes anything. That
first loop is the proof. Do not set up git, sync, or anything else on day one.

## What is in here

| Path | What it is |
|---|---|
| `seed/` | An empty Soulvant. This is the thing you take. |
| `docs/` | The explainer, served at the link above. |
| `tools/soulvant_seed.py` | Generates the `seed/` folder. You do not need it; it is how the folder above was made. |
| `tools/soulvant_schematic.py` | Prints an ASCII diagram of a base's state and pipelines, from live data. Run it once your base has something in it. |

## What the seed deliberately leaves out

The seed carries portable pieces only. It does not carry one owner's
configuration: no typography rules, no prose watchlist, no decay scoring, no
particular schema for the state page, no named roster of agents. Those are
choices, and they should be yours or nobody's. Set your own equivalents once
you know what you actually need, which will not be on day one.

## The honest limits

This rewards a focused collection you return to over time far more than a place
where everything gets dumped. It is only as good as what you choose to feed it,
so you stay the curator. It organizes and connects; the judgment stays yours.

Two of these exist and talk to each other so far. The bundles they traded were
assembled by hand. That is an observation, not a validation.

## If you build one

**Send me a slice.**

Once your base has real material in it, ask your assistant to prepare a bundle:
the pages on one topic you care about, the sources behind them, and a catalog,
as plain Markdown that drops into anyone else's base. Review it yourself before
it leaves. Then send it.

That is the part I actually want more of. Two knowledge bases answering each
other's questions is the whole thesis, and it needs a third.

Open an issue here, or find me at
[github.com/charlieamadeus](https://github.com/charlieamadeus).

## Prior art

This implements the LLM-wiki pattern: immutable raw sources under a maintained
wiki layer, with a person curating. It aims at the
[Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) where
it can, so a base is plain Markdown you own and can move anywhere.

## License

MIT for the tools and the seed scaffolding. Whatever you write into your own
base is yours.
