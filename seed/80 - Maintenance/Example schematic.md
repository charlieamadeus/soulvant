# What this looks like later

A schematic of a working Soulvant, generated from the live base.
Yours starts empty and grows into a shape like this one.

```
========================================================================
SOULVANT :: an example, after 3 months
========================================================================

MEMORY TIERS

  +-------------+---------------+----------------+-----------------+
  |    MODEL    |    HARNESS    |    SOULVANT    |   RAW SOURCES   |
  |  horsepower |  short term   |    midterm     |    long term    |
  +-------------+---------------+----------------+-----------------+
  | general     | this session  | durable, mine  | immutable,      |
  | knowledge,  | only; dies at | synthesized at | never rewritten,|
  | nothing     | the context   | ingest, cited  | every claim     |
  | personal    | boundary      | back down      | traces here     |
  +-------------+---------------+----------------+-----------------+
                                 ^^^^^^^^^^^^^^
                                 the gap this fills

  How an agent gets information and stores it is what gives it agency.
  Otherwise it is a general model with a very confused memory.

------------------------------------------------------------------------

LAYERS

  20 Sources        425   immutable evidence; agents may add, never rewrite
  10 Notes          952   one idea per page, every claim cited
  00 MOCs            43   synthesis per topic, the navigable layer
  30 Projects       186   what is being built
  40 People          48   recurring actors, bi-temporal
  Ledger            106   the action layer: one row per live thread
  log.md           1437   append-only record of what changed and why

  Sources and claims are separate canons. Nothing crosses without a
  promotion pass the owner reviews. That separation is the whole fix:
  the memory lives outside every agent, and no agent owns it.

------------------------------------------------------------------------

IDEA TYPES

                        MOCs   notes
  The build                9     253  ############################
  Client work              6     110  ############
  Agent engineering        7     244  ###########################
  AI industry              4      98  ###########
  Mind                     6     157  #################
  Political economy        4     105  ############
  Language and craft       3      52  ######
  Life                     4      44  #####
                          43    1063

  A note counts once per idea type it links up to, so the total
  exceeds the note count where a page bridges two domains.
  Unlinked notes: 0.

------------------------------------------------------------------------

PIPELINES

   inbox / clipping / transcript / chat
                |
                v
          [ INGEST ] --- reads it back to you before writing anything
                |          flags contradictions with what you already hold
                |
     +----------+----------+-----------+
     v          v          v           v
  sources     notes      MOCs       Ledger
  (frozen)   (cited)  (synthesis)  (what is live)
     |          |          |           |
     +----------+----+-----+-----------+
                     |
        +------------+------------+------------+
        v            v            v            v
    [ QUERY ]   [ RESEARCH ]  [ BRIEF ]    [ LINT ]
   answers from  goes outside  renders the  finds gaps,
   your own      when you are  action view  contradictions,
   material,     missing       read-only    stale claims;
   sources shown something                  proposes, never
        |                                   rewrites meaning
        v
    [ LEARN ] --- teaches it back so the understanding stays yours
        |
        v
    [ BUNDLE ] --- an owner-approved slice leaves as portable context
                   for another person, or for their agent

========================================================================
```
