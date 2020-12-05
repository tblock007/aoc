from sys import stdin
from collections import deque
from itertools import permutations

def translate(addr, mode):
    global v, rb
    if mode == 0:
        return v[addr]
    elif mode == 1:
        return addr
    elif mode == 2:
        return rb + v[addr]
    else:
        print('Error translating!')

def obtainAddresses(p, addArgs, pc, modeFlags):
    global v
    for i in range(addArgs):
        p.append(translate(pc + i + 1, modeFlags % 10))
        modeFlags //= 10

def execute(pc):
    global v, iq, oq, rb
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
    elif instr == 9: # relbase
        addArgs = 1
        obtainAddresses(a, addArgs, pc, modeFlags)
        rb += v[a[0]]
    elif instr == 99: # halt
        addArgs = -1
    else:        
        print('Unimplemented instruction at {0}!'.format(pc))
    return (pc + addArgs + 1)

def runProgramUntilOutputOrHalt():
    global v, pc
    while (v[pc] % 100 != 4):
        if (v[pc] % 100 == 99):
            return
        pc = execute(pc)
    pc = execute(pc)
        
refv = [int(w) for w in stdin.readline().split(',')]
v = refv[:]
v.extend((0 for _ in range(1000000)))
pc = 0
rb = 0
iq, oq = deque(), deque()

while (v[pc] % 100 != 99):    
    runProgramUntilOutputOrHalt()
    if (v[pc] % 100 == 99):
        break

count = 0
while oq:
    x = oq.popleft()
    y = oq.popleft()
    t = oq.popleft()
    if t == 2:
        count += 1
print(count)