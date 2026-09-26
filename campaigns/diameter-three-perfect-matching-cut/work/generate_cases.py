"""Fix seeded diameter-four Perfect Matching Cut cases before construction."""

import json
import random
from pathlib import Path


def graph(n,edges):
    return {"vertices":n,"edges":edges}


def cycle(n):
    return [[i,i+1] for i in range(n-1)]+[[0,n-1]]


EDGE_CASES = [
    (graph(1,[]),False),
    (graph(2,[[0,1]]),True),
    (graph(3,[[0,1],[1,2],[0,2]]),False),
    (graph(3,[[0,1],[1,2]]),False),
    (graph(4,cycle(4)),True),
    (graph(4,[[u,v] for u in range(4) for v in range(u+1,4)]),False),
    (graph(4,[[0,1],[1,2],[2,3]]),True),
    (graph(4,[[0,1],[0,2],[0,3]]),False),
    (graph(5,cycle(5)),False),
    (graph(5,[[i,i+1] for i in range(4)]),False),
    (graph(6,[[0,1],[0,2],[1,2],[3,4],[3,5],[4,5],[0,3],[1,4],[2,5]]),True),
    (graph(8,cycle(8)),True),
]


def random_source(seed):
    rng = random.Random(seed)
    if seed % 2 == 0:
        m = rng.choice((3,4))
        n = 2*m
        edges = [[i,m+i] for i in range(m)]
        for offset in (0,m):
            edges += [[offset,offset+i] for i in range(1,m)]
            edges += [[offset+i,offset+j] for i in range(1,m)
                      for j in range(i+1,m) if rng.randrange(2)]
    else:
        n = rng.randint(4,8)
        edges = [[0,v] for v in range(1,n)]
        edges += [[u,v] for u in range(1,n) for v in range(u+1,n)
                  if rng.randrange(2)]
    return graph(n,sorted(edges))


def build_cases():
    from check import solve_source
    cases, seen = [], set()

    def add(source,kind,seed=None,hand_answer=None):
        key = json.dumps(source,sort_keys=True,separators=(",", ":"))
        if key in seen:
            return False
        seen.add(key)
        answer = solve_source(source)
        if hand_answer is not None and ("side" in answer) != hand_answer:
            raise AssertionError(f"Hand label disagrees with oracle: {source}")
        case = {"source":source,"kind":kind,"expected":answer}
        if seed is not None:
            case["seed"] = seed
        cases.append(case)
        return True

    for source,expected in EDGE_CASES:
        add(source,"edge",hand_answer=expected)
    seed = 0
    while sum(case["kind"] == "random" for case in cases) < 100:
        add(random_source(seed),"random",seed=seed)
        seed += 1
    return cases


if __name__ == "__main__":
    path = Path(__file__).with_name("cases.json")
    cases = build_cases()
    path.write_text(json.dumps(cases,indent=2)+"\n")
    print(f"Wrote {len(cases)} cases to {path}")
