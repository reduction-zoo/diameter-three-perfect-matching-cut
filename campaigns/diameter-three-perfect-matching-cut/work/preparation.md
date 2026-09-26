# Preparation evidence

Prepared on 2026-09-26 before construction. The fixed corpus has 112
distinct legal connected diameter-at-most-four graphs: 12 hand-labelled
edge cases and 100 seeded random cases, with 40 YES and 72 NO decisions
and one to eight vertices. `generate_cases.py` retains the seeds and
generator; `cases.json` stores checked cuts or NO-SOLUTION. Graph legality
is checked by breadth-first distances from every vertex. Z3 4.16.0 has
one Boolean side per vertex, requires both sides nonempty, and constrains
each vertex to exactly one opposite-side neighbor. Every returned cut is
checked by direct neighbor counting. UNSAT is conclusive; unknown is an
error. Exhaustive Boolean side assignments agreed with Z3 on all 112
source cases.

The same encoding and direct validator are used for the diameter-three
target, with its tighter legality check. Independent exhaustive cut
enumeration agreed with Z3 on 84 distinct connected target graphs with up
to seven vertices. Hand fixtures cover a valid four-cycle cut, an invalid
triangle, a prism with a matching cut, the one-vertex case, and a path
whose diameter is allowed only at the source.

Reproduce from the repository root:

```sh
uv sync --locked
uv run --locked python campaigns/diameter-three-perfect-matching-cut/work/check.py --self-test
```

The self-test starts with the corpus gate, regenerates random source graphs,
rechecks labels and witnesses, and compares target decisions to exhaustive
enumeration. The candidate runner uses separate forward and recovery
subprocesses and up to three target cuts per case. An incorrect injected
candidate was rejected after target solving and source validation. No
actual reduction candidate exists; finite checks do not establish a
general reduction or hardness.
