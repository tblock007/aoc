import sys

def run(op, sa, sb, sc, r):
    a, b, c = int(sa), int(sb), int(sc)
    result = [i for i in r]
    
    try:
        if op == 'addr':
            result[c] = r[a] + r[b]
        if op == 'addi':
            result[c] = r[a] + b
        if op == 'mulr':
            result[c] = r[a] * r[b]
        if op == 'muli':
            result[c] = r[a] * b
        if op == 'banr':
            result[c] = r[a] & r[b]
        if op == 'bani':
            result[c] = r[a] & b
        if op == 'borr':
            result[c] = r[a] | r[b]
        if op == 'bori':
            result[c] = r[a] | b
        if op == 'setr':
            result[c] = r[a]
        if op == 'seti':
            result[c] = a
        if op == 'gtir':
            result[c] = (1 if a > r[b] else 0)
        if op == 'gtri':
            result[c] = (1 if r[a] > b else 0)
        if op == 'gtrr':
            result[c] = (1 if r[a] > r[b] else 0)
        if op == 'eqir':
            result[c] = (1 if a == r[b] else 0)
        if op == 'eqri':
            result[c] = (1 if r[a] == b else 0)
        if op == 'eqrr':
            result[c] = (1 if r[a] == r[b] else 0)
        return result
    except:
        return []

lines = sys.stdin.readlines()
ir = int(lines[0].split()[1])
code = lines[1:]

ip = 0
r = [0] * 6
while ip >= 0 and ip < len(code):
    op, a, b, c = code[ip].split()
    r[ir] = ip
    r = run(op, a, b, c, r)
    ip = r[ir] + 1
print(r)

