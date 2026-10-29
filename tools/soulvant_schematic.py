#!/usr/bin/env python3
"""Emit an ASCII schematic of a Soulvant's state and pipelines.

Reads a base and prints a diagram suitable for a terminal, a slide, or the
About page of a seed bundle. ASCII only, no box-drawing characters, so it
survives every codepage and every agent that reads it back.

Usage:
    python3 tools/soulvant_schematic.py                 # this folder's base
    python3 tools/soulvant_schematic.py --section tiers # one section
    python3 tools/soulvant_schematic.py --vault PATH    # another base
    python3 tools/soulvant_schematic.py --width 78

On Windows, use py instead of python3.

Sections: tiers, layers, ideas, pipelines.
"""

import argparse
import glob
import os
import re
import sys

TOP_TOPICS = 12


def find(vault, pattern):
    hits = glob.glob(os.path.join(vault, pattern))
    return hits[0] if hits else None


def count_md(vault, pattern):
    root = find(vault, pattern)
    if not root:
        return 0
    return sum(len([f for f in files if f.endswith(".md")])
               for _, _, files in os.walk(root))


def read_text(path):
    if not path or not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def topic_name(moc_name):
    if moc_name.startswith("MOC - "):
        return moc_name[len("MOC - "):]
    return moc_name


WIKILINK = re.compile(r"\[\[([^\]|#]+)")


def open_items(state_text):
    """Count the '- ' lines under the '## Open' heading of state.md."""
    count, inside = 0, False
    for line in state_text.splitlines():
        if line.startswith("#"):
            inside = line.strip() == "## Open"
            continue
        if inside and line.startswith("- "):
            count += 1
    return count


def survey(vault):
    """Walk the base once and return every number the schematic needs."""
    moc_dir = find(vault, "00*MOCs")
    note_dir = find(vault, "10*Notes")

    # Each MOC file is its own topic. A folder README is a label, not a MOC.
    mocs = []
    if moc_dir:
        for name in sorted(os.listdir(moc_dir)):
            if name.endswith(".md") and name.lower() != "readme.md":
                mocs.append(name[:-3])
    by_key = {m.lower(): m for m in mocs}

    # A note counts toward each MOC it wikilinks anywhere in its text.
    by_moc = {m: 0 for m in mocs}
    orphans = 0
    notes = 0

    if note_dir:
        for dirpath, _, files in os.walk(note_dir):
            for fname in files:
                if not fname.endswith(".md") or fname.lower() == "readme.md":
                    continue
                notes += 1
                text = read_text(os.path.join(dirpath, fname))
                seen = set()
                for raw in WIKILINK.findall(text):
                    key = raw.strip().split("/")[-1]
                    if key.lower().endswith(".md"):
                        key = key[:-3]
                    moc = by_key.get(key.lower())
                    if moc and moc not in seen:
                        seen.add(moc)
                        by_moc[moc] += 1
                if not seen:
                    orphans += 1

    log_text = read_text(find(vault, "log.md"))
    log_entries = len(re.findall(r"^## \[", log_text, re.M))

    state_open = open_items(read_text(find(vault, "state.md")))

    return {
        "sources": count_md(vault, "20*Sources"),
        "notes": notes,
        "mocs": len(mocs),
        "projects": count_md(vault, "30*Projects"),
        "people": count_md(vault, "40*People"),
        "log_entries": log_entries,
        "state_open": state_open,
        "by_moc": by_moc,
        "orphans": orphans,
    }


def rule(width, char="="):
    return char * width


def section_tiers(s, width):
    out = ["MEMORY TIERS", ""]
    out += [
        "  +-------------+---------------+----------------+-----------------+",
        "  |    MODEL    |    HARNESS    |    SOULVANT    |   RAW SOURCES   |",
        "  |  horsepower |  short term   |    midterm     |    long term    |",
        "  +-------------+---------------+----------------+-----------------+",
        "  | general     | this session  | durable, mine  | immutable,      |",
        "  | knowledge,  | only; dies at | synthesized at | never rewritten,|",
        "  | nothing     | the context   | ingest, cited  | every claim     |",
        "  | personal    | boundary      | back down      | traces here     |",
        "  +-------------+---------------+----------------+-----------------+",
        "                                 ^^^^^^^^^^^^^^",
        "                                 the gap this fills",
        "",
        "  How an agent gets information and stores it is what gives it agency.",
        "  Otherwise it is a general model with a very confused memory.",
    ]
    return out


def section_layers(s, width):
    rows = [
        ("20 Sources", s["sources"], "immutable evidence; agents may add, never rewrite"),
        ("10 Notes", s["notes"], "one idea per page, every claim cited"),
        ("00 MOCs", s["mocs"], "synthesis per topic, the navigable layer"),
        ("30 Projects", s["projects"], "what is being built"),
        ("40 People", s["people"], "recurring actors, bi-temporal"),
        ("state.md", s["state_open"], "what is open, in flight, and decided"),
        ("log.md", s["log_entries"], "append-only record of what changed and why"),
    ]
    out = ["LAYERS", ""]
    for name, count, desc in rows:
        out.append("  %-14s %6s   %s" % (name, count, desc))
    out += [
        "",
        "  Sources and claims are separate canons. Nothing crosses without a",
        "  promotion pass the owner reviews. That separation is the whole fix:",
        "  the memory lives outside every agent, and no agent owns it.",
    ]
    return out


def section_ideas(s, width):
    out = ["TOPICS", ""]
    ranked = sorted(s["by_moc"].items(), key=lambda kv: (-kv[1], kv[0].lower()))
    if not ranked:
        out.append("  No MOCs yet. Each MOC in 00 - MOCs/ becomes a row here.")
    else:
        shown, rest = ranked[:TOP_TOPICS], ranked[TOP_TOPICS:]
        rows = [(topic_name(m)[:28], n) for m, n in shown]
        if rest:
            rows.append(("Other (%d MOCs)" % len(rest), sum(n for _, n in rest)))
        peak = max(1, max(n for _, n in rows))
        out.append("  %-28s %7s" % ("", "notes"))
        total_n = 0
        for name, n in rows:
            total_n += n
            bar = "#" * max(1, round(n / peak * 28)) if n else ""
            out.append(("  %-28s %7d  %s" % (name, n, bar)).rstrip())
        out.append("  %-28s %7d" % ("", total_n))
    out += [
        "",
        "  A note counts once per MOC it links, so the total exceeds",
        "  the note count where a page links two topics.",
        "  Unlinked notes: %d." % s["orphans"],
    ]
    return out


def section_pipelines(s, width):
    return [
        "PIPELINES",
        "",
        "   inbox / clipping / transcript / chat",
        "                |",
        "                v",
        "          [ INGEST ] --- reads it back to you before writing anything",
        "                |          flags contradictions with what you already hold",
        "                |",
        "     +----------+----------+-----------+",
        "     v          v          v           v",
        "  sources     notes      MOCs       state",
        "  (frozen)   (cited)  (synthesis)  (what is live)",
        "     |          |          |           |",
        "     +----------+----+-----+-----------+",
        "                     |",
        "        +------------+------------+------------+",
        "        v            v            v            v",
        "    [ QUERY ]   [ RESEARCH ]  [ BRIEF ]    [ LINT ]",
        "   answers from  goes outside  renders the  finds gaps,",
        "   your own      when you are  action view  contradictions,",
        "   material,     missing       read-only    stale claims;",
        "   sources shown something                  proposes, never",
        "        |                                   rewrites meaning",
        "        v",
        "    [ LEARN ] --- teaches it back so the understanding stays yours",
        "        |",
        "        v",
        "    [ BUNDLE ] --- an owner-approved slice leaves as portable context",
        "                   for another person, or for their agent",
    ]


SECTIONS = {
    "tiers": section_tiers,
    "layers": section_layers,
    "ideas": section_ideas,
    "pipelines": section_pipelines,
}


def render(vault, which, width, title=None):
    s = survey(vault)
    name = title or os.path.basename(os.path.abspath(vault))
    out = [rule(width), "SOULVANT :: %s" % name, rule(width), ""]
    order = [which] if which else ["tiers", "layers", "ideas", "pipelines"]
    for i, key in enumerate(order):
        out.extend(SECTIONS[key](s, width))
        if i != len(order) - 1:
            out += ["", rule(width, "-"), ""]
    out += ["", rule(width)]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vault", default=".",
                    help="base root (default: the current folder)")
    ap.add_argument("--section", choices=sorted(SECTIONS), default=None)
    ap.add_argument("--width", type=int, default=72)
    ap.add_argument("--title", default=None)
    ap.add_argument("--out", default=None, help="write to a file instead of stdout")
    args = ap.parse_args()

    text = render(args.vault, args.section, args.width, args.title)
    if args.out:
        with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text + "\n")
        print("wrote %s" % args.out)
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(text)


if __name__ == "__main__":
    main()
