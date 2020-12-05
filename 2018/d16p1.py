from sys import stdin
import re

def run(op, a, b, c, r):
    result = [i for i in r]
    
    try:
        if op == 0: # addr
            result[c] = r[a] + r[b]
        if op == 1: # addi
            result[c] = r[a] + b
        if op == 2: # mulr
            result[c] = r[a] * r[b]
        if op == 3: # muli
            result[c] = r[a] * b
        if op == 4: # banr
            result[c] = r[a] & r[b]
        if op == 5: # bani
            result[c] = r[a] & b
        if op == 6: # borr
            result[c] = r[a] | r[b]
        if op == 7: # bori
            result[c] = r[a] | b
        if op == 8: # setr
            result[c] = r[a]
        if op == 9: # seti
            result[c] = a
        if op == 10: # gtir
            result[c] = (1 if a > r[b] else 0)
        if op == 11: # gtri
            result[c] = (1 if r[a] > b else 0)
        if op == 12: # gtrr
            result[c] = (1 if r[a] > r[b] else 0)
        if op == 13: # eqir
            result[c] = (1 if a == r[b] else 0)
        if op == 14: # eqri
            result[c] = (1 if r[a] == b else 0)
        if op == 15: # eqrr
            result[c] = (1 if r[a] == r[b] else 0)
        return result
    except:
        return []


def poss(r, i, rp):
    return sum(1 for p in range(16) if rp == run(p, i[1], i[2], i[3], r))

pattern = re.compile('[0-9]+')
count = 0
for _ in range(3096 // 4):
    r = [int(c) for c in pattern.findall(input())]
    i = [int(c) for c in pattern.findall(input())]
    rp = [int(c) for c in pattern.findall(input())]
    input()
    if poss(r, i, rp) >= 3:
        count += 1
        
print(count)
