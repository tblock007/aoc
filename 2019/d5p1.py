from sys import stdin

PSA = 1 # player specific input

def translate(addr, mode):
    global v
    if mode == 0:
        return v[addr]
    elif mode == 1:
        return addr
    else:
        print('Error translating!')

def obtainAddresses(p, addArgs, pc, modeFlags):
    global v
    for i in range(addArgs):
        p.append(translate(pc + i + 1, modeFlags % 10))
        modeFlags //= 10

def execute(pc):
    global v
    modeFlags, instr = v[pc] // 100, v[pc] % 100
    a = []
    if instr == 1: # add
        addArgs = 3
        obtainAddresses(a, addArgs, pc, modeFlags)    
        v[a[2]] = v[a[0]] + v[a[1]]
    elif instr == 2: # mul    
        addArgs = 3        
        obtainAddresses(a, addArgs, pc, modeFlags)
        v[a[2]] = v[a[0]] * v[a[1]]
    elif instr == 3: # input
        addArgs = 1        
        obtainAddresses(a, addArgs, pc, modeFlags)
        v[a[0]] = PSA
    elif instr == 4: # output
        addArgs = 1        
        obtainAddresses(a, addArgs, pc, modeFlags)
        print(v[a[0]])
    else:
        print('Unimplemented instruction!')
    return (pc + addArgs + 1)


v = [int(w) for w in stdin.readline().split(',')]
pc = 0
while (v[pc] != 99):
    pc = execute(pc)
