# Prepared input and output contract

Both source and target inputs use `{"vertices": n, "edges": [[u,v],
...]}` with a connected simple undirected graph on `0..n-1`, `n >= 1`.
The source has diameter at most four; the target has diameter at most three.
A positive output is `{"side": [bool, ...]}`, a nontrivial two-side
partition in which every vertex has exactly one neighbor on the opposite
side. Thus the crossing edges form a perfect matching. The alternative
`{"status": "NO-SOLUTION"}` is valid exactly when no such partition
exists. A one-vertex connected graph is legal but has no nontrivial cut.

A candidate `algorithm.py` reads one source JSON object from stdin and
writes one legal target JSON object to stdout. With `--extract`, it reads
`{"source": source, "target_solution": output}` and writes a valid source
output. The commands share no memory, exit nonzero on errors and send
diagnostics to stderr. They must be deterministic and polynomial time;
recovery must work for every valid target cut or negative answer.

`check.py --candidate PATH` independently solves constructed targets on the
fixed source corpus and directly validates recovered source cuts.
