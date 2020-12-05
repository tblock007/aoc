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

# returns True if 1 trillion ore can produce the specified amount of fuel
def trial(fuel):
    global al
    amounts = { p[0]:0 for p in al.keys() }
    amounts['FUEL'] = fuel
    amounts['ORE'] = 0
    while not complete(amounts):
        for p, rs in al.items():
            np = p[1]
            times = amounts[p[0]] // np
            if amounts[p[0]] % np != 0:
                times += 1
            for r, nr in rs:
                amounts[r] += nr * times
            amounts[p[0]] -= np * times
    return amounts['ORE'] <= 1000000000000    

al = {}
for line in sys.stdin.readlines():
    parse(line)
low, high = 100000, 1000000000000
found = False
while True:
    mid = (low + high) // 2
    m, m1 = trial(mid), trial(mid + 1)
    if m and not m1:
        print(mid)
        break
    if m:
        low = mid
    else:
        high = mid
