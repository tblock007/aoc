from sys import stdin

def run(v, pc):
    x, y, d = v[pc + 1], v[pc + 2], v[pc + 3]
    if v[pc] == 1:
        v[d] = v[x] + v[y]
    elif v[pc] == 2:
        v[d] = v[x] * v[y]

v = [int(w) for w in stdin.readline().split(',')]
v[1], v[2] = 12, 2 # player specific input
pc = 0
while (v[pc] != 99):
    run(v, pc)
    pc += 4
print(v[0])