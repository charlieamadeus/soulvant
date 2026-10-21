#!/usr/bin/env python3
"""Emit an ASCII schematic of a Soulvant's state and pipelines.

Reads the live vault and prints a diagram suitable for a terminal, a slide,
or the About page of a seed bundle. ASCII only, no box-drawing characters,
so it survives every codepage and every agent that reads it back.

Usage:
    py -3 scripts/soulvant_schematic.py                 # full schematic
    py -3 scripts/soulvant_schematic.py --section tiers # one section
    py -3 scripts/soulvant_schematic.py --vault PATH    # another Soulvant
    py -3 scripts/soulvant_schematic.py --width 78

Sections: tiers, layers, ideas, pipelines.
"""

import argparse
import glob
import os
import re
import sys

# MOC name fragment -> idea type. First match wins, so order matters:
# specific names must precede the substrings that would also catch them.
IDEA_TYPES = [
    ("Client AI and Knowledge Systems", "Client work"),
    ("Client Infrastructure Delivery", "Client work"),
    ("Client Service Design", "Client work"),
    ("Client Infrastructure Work", "Client work"),
    ("LLM-wiki Deployment", "Client work"),
    ("AI-Native Firm", "Client work"),

    ("AI Markets and Compute", "AI industry"),
    ("AI Political Economy", "AI industry"),
    ("AI Product Strategy", "AI industry"),
    ("AI Market and Business", "AI industry"),

    ("Agent Evaluation", "Agent engineering"),
    ("Agent Security", "Agent engineering"),
    ("Agentic Engineering", "Agent engineering"),
    ("AI Architecture and Post-LLM", "Agent engineering"),
    ("Coding-Agent Practice", "Agent engineering"),
    ("Prompt Engineering", "Agent engineering"),
    ("Fiduciary Agents", "Agent engineering"),

    ("Personal Agent Architecture", "The build"),
    ("Personal Agent Identity", "The build"),
    ("Personal Agent Intelligence", "The build"),
    ("Personal AI Memory", "The build"),
    ("Brain-Inspired Memory", "The build"),
    ("LLM-wiki Operations", "The build"),
    ("Soulvant", "The build"),
    ("Eternal Knowledge", "The build"),

    ("Consciousness Metaphysics", "Mind"),
    ("Machine Consciousness", "Mind"),
    ("AI Consciousness", "Mind"),
    ("AI Moral Status", "Mind"),
    ("Determinism and Agency", "Mind"),
    ("Relational Process-Pattern", "Mind"),

    ("Constrained and Unconstrained", "Political economy"),
    ("Economic Methodology", "Political economy"),
    ("Utopian Practice", "Political economy"),
    ("Earthseed", "Political economy"),

    ("Language and Thought", "Language and craft"),
    ("Language as Instrument", "Language and craft"),
    ("Creative Practice", "Language and craft"),

    ("Family Wealth", "Life"),
    ("Family and Relationships", "Life"),
    ("Health and Lifestyle", "Life"),
    ("Contemplative Practice", "Life"),
]

TYPE_ORDER = [
    "The build",
    "Client work",
    "Agent engineering",
    "AI industry",
    "Mind",
    "Political economy",
    "Language and craft",
    "Life",
]


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


def classify(moc_name):
    for fragment, idea in IDEA_TYPES:
        if fragment.lower() in moc_name.lower():
            return idea
    return "Unclassified"


LINKS_UP = re.compile(r"^##+\s*Links up\s*$", re.I)
WIKILINK = re.compile(r"\[\[([^\]|#]+)")


def survey(vault):
    """Walk the vault once and return every number the schematic needs."""
    moc_dir = find(vault, "00*MOCs")
    note_dir = find(vault, "10*Notes")

    mocs = {}
    if moc_dir:
        for name in sorted(os.listdir(moc_dir)):
            if name.endswith(".md"):
                mocs[name[:-3]] = classify(name[:-3])

    # Attribute each note to the idea types of the MOCs it links up to.
    by_type = {t: 0 for t in TYPE_ORDER}
    by_type["Unclassified"] = 0
    orphans = 0
    notes = 0

    if note_dir:
        for dirpath, _, files in os.walk(note_dir):
            for fname in files:
                if not fname.endswith(".md"):
                    continue
                notes += 1
                text = read_text(os.path.join(dirpath, fname))
                lines = text.splitlines()
                targets, capturing = [], False
                for line in lines:
                    if line.startswith("#"):
                        capturing = bool(LINKS_UP.match(line.strip()))
                        continue
                    if capturing:
                        targets.extend(WIKILINK.findall(line))
                # Fall back to any MOC wikilink anywhere in the page.
                if not targets:
                    targets = [t for t in WIKILINK.findall(text)
                               if t.strip().upper().startswith("MOC")]
                seen = set()
                for raw in targets:
                    key = raw.strip().split("/")[-1]
                    idea = mocs.get(key)
                    if idea is None:
                        for moc_name, moc_idea in mocs.items():
                            if moc_name.lower() == key.lower():
                                idea = moc_idea
                                break
                    if idea and idea not in seen:
                        seen.add(idea)
                        by_type[idea] = by_type.get(idea, 0) + 1
                if not seen:
                    orphans += 1

    moc_counts = {t: 0 for t in TYPE_ORDER}
    moc_counts["Unclassified"] = 0
    for idea in mocs.values():
        moc_counts[idea] = moc_counts.get(idea, 0) + 1

    log_text = read_text(find(vault, "log.md"))
    log_entries = len(re.findall(r"^## \[", log_text, re.M))

    # A Ledger data row opens with an id cell: lowercase, digits, hyphens.
    ledger_text = read_text(find(vault, "80*Maintenance/Ledger.md"))
    row_id = re.compile(r"^\|\s*`?([a-z0-9][a-z0-9-]*)`?\s*\|")
    ledger_rows = len([l for l in ledger_text.splitlines()
                       if l.count("|") >= 8 and row_id.match(l)])

    return {
        "sources": count_md(vault, "20*Sources"),
        "notes": notes,
        "mocs": len(mocs),
        "projects": count_md(vault, "30*Projects"),
        "people": count_md(vault, "40*People"),
        "log_entries": log_entries,
        "ledger_rows": ledger_rows,
        "by_type": by_type,
        "moc_counts": moc_counts,
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
        ("Ledger", s["ledger_rows"], "the action layer: one row per live thread"),
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
    out = ["IDEA TYPES", "",
           "  %-20s %5s %7s" % ("", "MOCs", "notes")]
    total_m = total_n = 0
    for t in TYPE_ORDER + ["Unclassified"]:
        m = s["moc_counts"].get(t, 0)
        n = s["by_type"].get(t, 0)
        if m == 0 and n == 0:
            continue
        total_m += m
        total_n += n
        bar = "#" * max(1, round(n / max(1, max(s["by_type"].values())) * 28))
        out.append("  %-20s %5d %7d  %s" % (t, m, n, bar))
    out.append("  %-20s %5d %7d" % ("", total_m, total_n))
    out += [
        "",
        "  A note counts once per idea type it links up to, so the total",
        "  exceeds the note count where a page bridges two domains.",
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
        "  sources     notes      MOCs       Ledger",
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
    ap.add_argument("--vault", default=os.path.join(os.path.dirname(__file__), ".."),
                    help="vault root (default: the repo this script lives in)")
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
