from sys import stdin
import re

def run(op, a, b, c, r):
    result = [i for i in r]
    
    try:
        # opcodes are known after solving by hand
        if op == 9: # addr
            result[c] = r[a] + r[b]
        if op == 11: # addi
            result[c] = r[a] + b
        if op == 15: # mulr
            result[c] = r[a] * r[b]
        if op == 7: # muli
            result[c] = r[a] * b
        if op == 5: # banr
            result[c] = r[a] & r[b]
        if op == 1: # bani
            result[c] = r[a] & b
        if op == 6: # borr
            result[c] = r[a] | r[b]
        if op == 3: # bori
            result[c] = r[a] | b
        if op == 8: # setr
            result[c] = r[a]
        if op == 2: # seti
            result[c] = a
        if op == 12: # gtir
            result[c] = (1 if a > r[b] else 0)
        if op == 14: # gtri
            result[c] = (1 if r[a] > b else 0)
        if op == 13: # gtrr
            result[c] = (1 if r[a] > r[b] else 0)
        if op == 4: # eqir
            result[c] = (1 if a == r[b] else 0)
        if op == 0: # eqri
            result[c] = (1 if r[a] == b else 0)
        if op == 10: # eqrr
            result[c] = (1 if r[a] == r[b] else 0)
        return result
    except:
        return []


def poss(r, i, rp):
    return set(op for op in range(16) if rp == run(op, i[1], i[2], i[3], r))

pattern = re.compile('[0-9]+')


# mapping = [set(i for i in range(16)) for op in range(16)]

# for _ in range(3096 // 4):
#     r = [int(c) for c in pattern.findall(input())]
#     i = [int(c) for c in pattern.findall(input())]
#     rp = [int(c) for c in pattern.findall(input())]
#     input()
#     mapping[i[0]] = mapping[i[0]].intersection(poss(r, i, rp))

# for index, ops in enumerate(mapping):
#     if index not in [5, 9]: # populate this list with known indices
#         print('{0}: '.format(index), end='')
#         print('-'.join(str(op) for op in ops if op not in [5, 9])) # populate this list with known opcodes
# # repeatedly run the above, adding known opcode-index pairs to hand-solve the true mapping

r = [0, 0, 0, 0]
for _ in range(956):
    op, a, b, c = [int(c) for c in pattern.findall(input())]
    r = run(op, a, b, c, r)
print(r)
