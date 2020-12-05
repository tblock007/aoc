from sys import stdin
from collections import deque
from itertools import permutations

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
    global v, iq, oq
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
        v[a[0]] = iq.popleft()
    elif instr == 4: # output
        addArgs = 1        
        obtainAddresses(a, addArgs, pc, modeFlags)
        oq.append(v[a[0]])
    elif instr == 5: # jnz
        addArgs = 2
        obtainAddresses(a, addArgs, pc, modeFlags)
        if (v[a[0]] != 0):
            pc = v[a[1]] - addArgs - 1
    elif instr == 6: # jz
        addArgs = 2
        obtainAddresses(a, addArgs, pc, modeFlags)
        if (v[a[0]] == 0):
            pc = v[a[1]] - addArgs - 1
    elif instr == 7: # sle
        addArgs = 3
        obtainAddresses(a, addArgs, pc, modeFlags)
        if (v[a[0]] < v[a[1]]):
            v[a[2]] = 1
        else:
            v[a[2]] = 0
    elif instr == 8: # seq
        addArgs = 3
        obtainAddresses(a, addArgs, pc, modeFlags)
        if (v[a[0]] == v[a[1]]):
            v[a[2]] = 1
        else:
            v[a[2]] = 0
    else:        
        print('Unimplemented instruction!')
    return (pc + addArgs + 1)

def runProgram():
    global refv
    v = refv[:]
    pc = 0
    while (v[pc] != 99):
        pc = execute(pc)

def testPermutation(p):
    global iq, oq
    output = 0
    for i in range(len(p)):   
        iq.clear()     
        iq.append(p[i])
        iq.append(output)
        runProgram()
        output = oq.popleft()
    return output
        
refv = [int(w) for w in stdin.readline().split(',')]
v = refv[:]
iq, oq = deque(), deque()
phases = list(range(5))
print(max(testPermutation(p) for p in permutations(phases)))