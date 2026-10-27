# How Soulvant compares

Soulvant gives Claude Code and Codex the same memory: a folder of plain Markdown files you own. This page says what it is and what it is not, so you can tell whether it fits. Every line about Soulvant here can be checked in this repo.

## What it is

- **A folder of plain Markdown files.** The `seed/` folder is an empty Soulvant. You unzip it, move it where you keep your files, and open it in Claude Code or Codex.
- **One set of rules for both agents.** The rules are in `seed/CLAUDE.md`. `seed/AGENTS.md` tells any other agent to read that file first. So Claude Code and Codex work on the same files under the same rules, and the next agent can pick up where the last one left off.
- **No server.** There is no MCP server, database or search index. The agent reads and writes the files. It finds pages through `index.md`, which lists every page on one line.
- **Sources stay as they came in.** The rules tell the agent never to rewrite the body of a file in `20 - Sources/`.
- **Claims point back to sources.** Every note cites where it came from under `## Sources`.
- **Decisions keep their reasons.** `state.md` holds what is open, in flight and decided, with the date and the reasoning.
- **An Obsidian vault, if you want one.** Open the folder in Obsidian to browse it. Any text editor works too.

## What it is not

- **Not an MCP memory server.** Soulvant gives your assistant no memory tool to call over MCP. If that is what you want, see [Basic Memory](https://github.com/basicmachines-co/basic-memory) and [Mem0](https://github.com/mem0ai/mem0); their own pages say what they do.
- **Not for the web chat.** It does not work in the ChatGPT or Claude chat in a web browser. Those cannot read and write a folder on your computer.
- **Not a sync service.** Nothing in it copies the folder between computers. The seed suggests git for history and backup, later, not on day one.

## Which fits

Pick Soulvant if you want the agent you already use to keep your sources, notes and decisions as files you can read, under rules you can read and change.
