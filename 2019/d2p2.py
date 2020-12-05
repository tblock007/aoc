from sys import stdin

def run(v, pc):
    x, y, d = v[pc + 1], v[pc + 2], v[pc + 3]
    if v[pc] == 1:
        v[d] = v[x] + v[y]
    elif v[pc] == 2:
        v[d] = v[x] * v[y]

target = 19690720 # player specific input
refv = [int(w) for w in stdin.readline().split(',')]

for noun in range(100):
    for verb in range(100):
        v = refv[:]
        v[1], v[2] = noun, verb   
        try:            
            pc = 0
            while (v[pc] != 99):
                run(v, pc)
                pc += 4
            if (v[0] == target):
                print(100 * noun + verb)
        except:
            continue