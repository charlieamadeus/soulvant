# Soulvant

Shared memory for Claude Code and Codex, kept as plain Markdown files you own. Open the folder in either agent and it picks up where the last one left off. Open it in Obsidian and it is a vault you can browse.

*Say it soul-vant, not solvent. Solutions plus savant: brilliance with soul.*

**[Download Soulvant (ZIP)](https://github.com/charlieamadeus/soulvant/archive/refs/heads/main.zip)**, then follow [Start one](#start-one). You need Claude Code or Codex in its desktop app. There is no MCP server or database to set up. The agent reads and writes the files itself.

Soulvant is a mind you can share, with your agents and the people you work with. It keeps what you've learned, what you've decided, and why, in files you own, so the next agent can see how you got here and help with what comes next.

Reportedly better than advertised. In fairness, we barely advertised.

## What it is

You read, decide, change your mind, and start things you mean to finish. Most of it scatters, and your AI forgets it when the chat closes.

Soulvant is a folder of plain text files on your computer that an AI agent keeps for you: what you have read, what you are working on, what you decided, and why. You decide what is worth keeping and what it means. The agent does the reading, filing, linking and upkeep. Any agent you open on that folder can pick up where the last one left off.

<details>
<summary><b>A short story about what this is</b></summary>

> In a certain library there was a book devoted to a single life.
>
> Its entries were ordinary: a conversation, an abandoned undertaking, a sentence copied from another book. Beside each, the owner had written why it mattered. These annotations occasionally contradicted one another. A few had been corrected; others had acquired questions.
>
> The librarians changed often. Each successor consulted the book before assisting its owner, and so an undertaking begun with one could continue with another. They learned to distinguish a discarded plan from a forgotten one.
>
> One evening, the owner described a scene he wished to live. The librarian entered it among the unfinished pages and found, elsewhere in the volume, three passages he had ceased to remember. Taken together, they suggested a way to begin.
>
> He recognized the possibility at once. He was less certain whether he had discovered his intention or formed it in the act of recognition.
>
> Before sleeping, he added a sentence.
>
> By morning, several people would be affected by what he had written.

</details>

## What it does

- **Files what you give it.** Drop in an article, a transcript or your own notes. Before writing anything, the agent tells you what it found, so a misread costs one sentence. Your original is never edited.
- **Answers from your own material.** Ask a question and the answer cites your sources.
- **Keeps one page of what is open, in flight and decided.**
- **Checks itself.** Now and then it looks for gaps and contradictions and proposes fixes. Changing what a page means stays your call.

## Five things it is for

**Not re-arguing settled decisions.**

> **Steve Jobs:** We turned down a thousand good ideas. Soulvant remembers every one, and why. When someone pitches one again, I don't have to win the same argument twice.

**Handing work from one agent to the next.**

> **Abraham Lincoln:** I replaced general after general before I found Grant. Thanks to Soulvant, each new one arrived already knowing what I wanted, and why the last one was let go.

**Finding connections across what you have read.**

> **Leonardo da Vinci:** Soulvant reads my mirror writing. And it noticed what I nearly missed: my notes on swirling rivers explain the valves of the heart.

**Keeping track of clients, people and promises.**

> **Frank Lloyd Wright:** I design a house for the land and the family in it. Soulvant remembers every client, every site and every promise. When Mr. Johnson calls about the leaking roof, it reminds me what I told him last time: move the chair.

**Giving a coding agent the reasons behind the code.**

> **Grace Hopper:** Before an agent changes my code, Soulvant gives it the decisions behind it: what we tried, what failed, and why that peculiar line is still there. It may still disagree. At least we can have a new argument.

[More reviews, collected by Will Durant](REVIEWS.md)

## Start one

You need Claude Code or Codex. They come in the desktop apps that come with paid Claude and ChatGPT plans, and they can read and write files in a folder on your computer. Soulvant needs that. The chat in a web browser cannot do it. You will not need Python, a terminal or git.

1. **Download the ZIP** with the link at the top, and unzip it. On a Mac, double-click it. On Windows, right-click it and choose Extract All.
2. **Find the folder called `seed`** inside what you unzipped. Move it somewhere you keep your own files, such as Documents, and rename it to whatever you like. That folder is your Soulvant. You can ignore the rest of the download.
3. **Put three or four files you care about** in its `90 - Inbox` folder: an article, a transcript, notes you wrote.
4. **Open your Soulvant folder in an agent.** For Claude: install the [Claude desktop app](https://claude.ai/download), sign in, open the Code tab, and choose your Soulvant folder as the folder to work in. For Codex: follow [OpenAI's Codex quickstart](https://learn.chatgpt.com/docs/quickstart) and open your Soulvant folder as the project. Then paste this:

> This folder is my new Soulvant. Work only from the files here and what I tell you; ignore what you remember from other chats. Read START HERE.md and CLAUDE.md. Then process one file from 90 - Inbox: tell me in plain words what you found and what you will file, and wait for my OK. Once it is filed, if the two blank sections in CLAUDE.md are empty, ask me what this is for and what it is NOT for, one question at a time (I may say "not decided yet"), and write my answers in. After that, ask me about the others.

5. **Answer it.** It tells you what it found before it files anything. Say OK, or tell it what it got wrong. If you only want to talk a file over, say "don't file it" and it leaves the file where it is. After the first file it asks what this Soulvant is for; "not decided yet" is a fine answer.
6. **Ask it something your file can answer.** Ask it to show the source it used, then open that source and check.

To browse the pages yourself, open the folder in [Obsidian](https://obsidian.md) (free) as a vault. Any text editor works too; these are plain text files.

**Day one** is done when a question you ask is answered from your own file, with the source cited.

**Week one** is done when you open the folder with a different agent, ask "Where were we?", and it can name your last decision and why you made it.

The full first-day walkthrough is [START HERE](seed/START%20HERE.md), inside the seed.

## Learn more

- [The explainer](https://charlieamadeus.github.io/soulvant/): the whole idea on one page.
- [What is in this repo, and what the seed leaves out](docs/REFERENCE.md)
- [How Soulvant compares with MCP memory tools](docs/COMPARE.md)
- [More reviews](REVIEWS.md)

## As it grows

The seed carries only what every Soulvant needs. Everything else should be yours, chosen when you need it.

An add-on is coming that lets an agent working in another folder read your Soulvant and leave it a report.

When the same problem hurts twice, ask your agent what would fix it. The rules one long-kept Soulvant learned the hard way, each with the failure behind it, live in soulvant-machinery, which is private for now; ask for access. Take a piece, not the whole.

## Send me a slice

Once your Soulvant has real material in it, ask your agent to prepare a bundle: the pages on one topic, the sources behind them, and a catalog, as plain Markdown that drops into anyone else's. Then send it.

Two knowledge bases answering each other's questions is the whole thesis. It needs more than two. Open an issue on this page (the Issues tab at the top), or find me at [github.com/charlieamadeus](https://github.com/charlieamadeus).

## Prior art and license

This implements the [LLM-wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) and aims at the [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md), so a Soulvant is plain Markdown you own and can move anywhere. MIT for the tools and the seed. Whatever you write into your own Soulvant is yours.
