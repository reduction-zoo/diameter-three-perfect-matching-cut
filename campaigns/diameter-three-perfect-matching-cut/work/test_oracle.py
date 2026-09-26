from check import legal_source, legal_target, solve_source, solve_target, valid_source, valid_target


def test_hand_cases():
    edge = {"vertices":2,"edges":[[0,1]]}
    assert valid_source(edge,{"side":[False,True]})
    assert valid_target(edge,{"side":[False,True]})
    assert not valid_source(edge,{"side":[False,False]})
    triangle = {"vertices":3,"edges":[[0,1],[1,2],[0,2]]}
    assert solve_source(triangle) == {"status":"NO-SOLUTION"}
    cycle = {"vertices":4,"edges":[[0,1],[1,2],[2,3],[0,3]]}
    assert valid_target(cycle,{"side":[False,False,True,True]})
    path5 = {"vertices":5,"edges":[[0,1],[1,2],[2,3],[3,4]]}
    assert legal_source(path5)
    assert not legal_target(path5)
    assert not legal_source({"vertices":2,"edges":[]})


if __name__ == "__main__":
    test_hand_cases()
