from sys import stdin
from collections import deque
from itertools import permutations

def translate(amp, addr, mode):
    global vv
    if mode == 0:
        return vv[amp][addr]
    elif mode == 1:
        return addr
    else:
        print('Error translating!')

def obtainAddresses(amp, p, addArgs, pc, modeFlags):
    for i in range(addArgs):
        p.append(translate(amp, pc + i + 1, modeFlags % 10))
        modeFlags //= 10

def execute(i, pc):
    global vv, hc, oq
    v = vv[i]
    modeFlags, instr = v[pc] // 100, v[pc] % 100
    a = []
    if instr == 1: # add
        addArgs = 3
        obtainAddresses(i, a, addArgs, pc, modeFlags)    
        v[a[2]] = v[a[0]] + v[a[1]]
    elif instr == 2: # mul    
        addArgs = 3        
        obtainAddresses(i, a, addArgs, pc, modeFlags)
        v[a[2]] = v[a[0]] * v[a[1]]
    elif instr == 3: # input
        addArgs = 1        
        obtainAddresses(i, a, addArgs, pc, modeFlags)
        v[a[0]] = oq[(i + 4) % 5].popleft()
    elif instr == 4: # output
        addArgs = 1        
        obtainAddresses(i, a, addArgs, pc, modeFlags)
        oq[i].append(v[a[0]])
    elif instr == 5: # jnz
        addArgs = 2
        obtainAddresses(i, a, addArgs, pc, modeFlags)
        if (v[a[0]] != 0):
            pc = v[a[1]] - addArgs - 1
    elif instr == 6: # jz
        addArgs = 2
        obtainAddresses(i, a, addArgs, pc, modeFlags)
        if (v[a[0]] == 0):
            pc = v[a[1]] - addArgs - 1
    elif instr == 7: # sle
        addArgs = 3
        obtainAddresses(i, a, addArgs, pc, modeFlags)
        if (v[a[0]] < v[a[1]]):
            v[a[2]] = 1
        else:
            v[a[2]] = 0
    elif instr == 8: # seq
        addArgs = 3
        obtainAddresses(i, a, addArgs, pc, modeFlags)
        if (v[a[0]] == v[a[1]]):
            v[a[2]] = 1
        else:
            v[a[2]] = 0
    elif instr == 99: #halt
        addArgs = -1
        hc += 1
    else:        
        print('Unimplemented instruction!')
    return (pc + addArgs + 1)

def runProgramUntilOutput(amp):
    global vv, pc
    while (vv[amp][pc[amp]] != 4 and vv[amp][pc[amp]] != 99):
        pc[amp] = execute(amp, pc[amp])
    pc[amp] = execute(amp, pc[amp])

def testPermutation(p):
    global hc, vv, refv, pc    
    
    # Reset for new trial
    pc = [0 for _ in range(5)]
    for ii in range(5):
        vv[ii] = refv[:]
    lastOutput = -1
    output = 0
    hc = 0
    i = -1
    for ii in range(5):
        oq[ii].clear()
        oq[ii].append(p[(ii + 1) % 5])
    oq[4].append(0)

    # Run until first halts. This is not strictly aligned with the
    # problem statement, but a bit of analysis of the samples and
    # input program suggest that all programs halt on the same iteration.
    while True:
        i = (i + 1) % 5
        runProgramUntilOutput(i)
        if hc > 0:
            return lastOutput
        if i == 4:
            lastOutput = oq[i][-1]
        
refv = [int(w) for w in stdin.readline().split(',')]
vv = [[] for _ in range(5)]
oq = [deque() for _ in range(5)]
hc = 0

phases = list(range(5, 10))
print(max(testPermutation(p) for p in permutations(phases)))