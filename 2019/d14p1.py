import re
import sys
from collections import deque

def parse(line):
    global al
    pline = [c for c in line.rstrip() if c != ',' and c != '=' and c != '>']
    tokens = [token for token in ''.join(pline).split(' ') if token]
    p, np = tokens[-1], int(tokens[-2])
    if (p, np) not in al.keys():
        al[(p, np)] = []
    for i in range(-3, -len(tokens) - 1, -2):
        r, nr = tokens[i], int(tokens[i - 1])
        al[(p, np)].append((r, nr))
    
def complete(amounts):
    for key, value in amounts.items():
        if key != 'ORE' and value > 0:
            return False
    return True


al = {}
for line in sys.stdin.readlines():
    parse(line)
amounts = { p[0]:0 for p in al.keys() }
amounts['FUEL'] = 1
amounts['ORE'] = 0

while not complete(amounts):
    for p, rs in al.items():
        np = p[1]
        while amounts[p[0]] > 0:
            for r, nr in rs:
                amounts[r] += nr
            amounts[p[0]] -= np
print(amounts['ORE'])

