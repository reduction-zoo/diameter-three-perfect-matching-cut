# Research instructions

Read the [fixed question](campaigns/diameter-three-perfect-matching-cut/question.md), [prior state](campaigns/diameter-three-perfect-matching-cut/state.md) and [preparation notes](campaigns/diameter-three-perfect-matching-cut/work/preparation.md). The fixed [test corpus](campaigns/diameter-three-perfect-matching-cut/work/cases.json) and [verifier](campaigns/diameter-three-perfect-matching-cut/work/check.py) are the starting evidence; the preparation notes state their coverage and any pending checks.

Run `uv sync --locked`, then `uv run --locked python campaigns/diameter-three-perfect-matching-cut/work/check.py --self-test` before relying on that evidence. Follow the current user's AutoResearch pipeline. Preserve prior evidence, commit new work incrementally and make only evidence-backed claims.
