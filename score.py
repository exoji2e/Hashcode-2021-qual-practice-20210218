from dataparser import *
from collections import *

# inp: the input file as a single string
# out: the answer file produced by your solver, as a single string
# return the score of the output as an integer
def score(inp, out):
    ns = parse(inp)
    itr = (line for line in out.split('\n'))
    D = ni(itr)
    assert 1 <= D <= ns.T2 + ns.T3 + ns.T4
    used = set()
    cnt = Counter()
    tot_score = 0
    for d in range(D):
        L = nl(itr)
        no = L[0]
        pizza_id = L[1:]
        assert no == len(pizza_id)
        assert 2 <= no <= 4
        cnt[no] += 1
        ingred = set()
        for p_id in pizza_id:
            assert p_id not in used
            used.add(p_id)
            p_ing = ns.pizzas[p_id]['ingredients']
            ingred |= set(p_ing)
        sc = len(ingred)**2
        tot_score += sc
    assert cnt[2] <= ns.T2
    assert cnt[3] <= ns.T3
    assert cnt[4] <= ns.T4

    return tot_score


