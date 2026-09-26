# Diameter-four Perfect Matching Cut → Diameter-three Perfect Matching Cut

Category: Complexity open

## Source

The source is a connected graph of diameter at most four. Its outputs are nontrivial cuts having exactly one opposite neighbor at every vertex, or NO-SOLUTION.

## Target

Both problems ask for a nontrivial bipartition with exactly one opposite neighbor per vertex, or NO-SOLUTION. The connected source graph has diameter at most four; the connected target graph has diameter at most three.

## Required result

Construct deterministic polynomial-time maps F and G: F sends every legal source instance to a legal target instance, and G(x,y) is a valid source output for every valid output y of F(x). Preserve the stated threshold, domain and promises. The requested complexity conclusion is NP-hardness for the stated target problem.

## Acceptance

Give explicit construction and recovery algorithms, a general proof for every legal input and every valid target output, and polynomial runtime and encoding-size bounds. Specify finite output encodings and handle NO-SOLUTION outputs when applicable. Tests compare recovered source outputs with independent source solutions.

## Why it matters

The question seeks the missing diameter boundary for Perfect Matching Cut.

## Difficulty

Distance shortcuts can introduce new perfect matching cuts or destroy old ones.

## Literature context

The cited diameter classification leaves the diameter-three case distinct from the known diameter-four hardness result.

Literature checked 2026-09-15. This summarizes the archived literature search on the date above. Unpublished, unindexed and overlooked work remains outside coverage; no new novelty assessment was performed.

## References

- [Dichotomies for Maximum Matching Cut: H-freeness, bounded diameter, bounded radius](https://durham-repository.worktribe.com/OutputFile/2851394): - R10. Lucke, Paulusma, Ries, Dichotomies for Maximum Matching Cut: H-freeness, bounded diameter, bounded radius, TCS 1017 (2024), 114795, Theorem 3 and concluding Open Problem 1; arXiv record. - R3. Lucke, Matching Cut and Variants on Bipartite Graphs of Bounded Radius and Diameter, arXiv:2501.08735v1, 15 January 2025, Table 1, Theorems 18–19, Corollary 17, Section 5, Open Problems 1–2.
- [arXiv record](https://arxiv.org/abs/2304.01099): - R10. Lucke, Paulusma, Ries, Dichotomies for Maximum Matching Cut: H-freeness, bounded diameter, bounded radius, TCS 1017 (2024), 114795, Theorem 3 and concluding Open Problem 1; arXiv record. - R3. Lucke, Matching Cut and Variants on Bipartite Graphs of Bounded Radius and Diameter, arXiv:2501.08735v1, 15 January 2025, Table 1, Theorems 18–19, Corollary 17, Section 5, Open Problems 1–2.
- [Matching Cut and Variants on Bipartite Graphs of Bounded Radius and Diameter](https://arxiv.org/html/2501.08735): - R10. Lucke, Paulusma, Ries, Dichotomies for Maximum Matching Cut: H-freeness, bounded diameter, bounded radius, TCS 1017 (2024), 114795, Theorem 3 and concluding Open Problem 1; arXiv record. - R3. Lucke, Matching Cut and Variants on Bipartite Graphs of Bounded Radius and Diameter, arXiv:2501.08735v1, 15 January 2025, Table 1, Theorems 18–19, Corollary 17, Section 5, Open Problems 1–2.

Fixed from board record `website/questions/diameter-three-perfect-matching-cut.json` in board checkout at 6c7d3bd9c0a8f595279969a9c0a4d1853a3f5c17; the record was copied from the current working tree.
