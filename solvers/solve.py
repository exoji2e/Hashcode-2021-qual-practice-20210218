import argparse
import random
from collections import *
from dataparser import parse

# inp is an input file as a single string
# return your output as a string
def solve(inp, args):
    # TODO: Solve the problem
    random.seed(args['seed'])
    ns = parse(inp)
    pizzas_left = set()
    for i in range(ns.M):
        pizzas_left.add(i)

    def pick(no):
        picked = []
        if len(pizzas_left) < no: return None
        for _ in range(no):
            p_id = pizzas_left.pop()
            picked.append(p_id)
        return picked

    teams = []
    for _ in range(ns.T4):
        picked = pick(4)
        if picked == None: break
        teams.append(' '.join(map(str, [4] + picked)))
    for _ in range(ns.T3):
        picked = pick(3)
        if picked == None: break
        teams.append(' '.join(map(str, [3] + picked)))

    for _ in range(ns.T2):
        picked = pick(2)
        if picked == None: break
        teams.append(' '.join(map(str, [2] + picked)))

    out = [str(len(teams))] + teams
    return '\n'.join(out)
