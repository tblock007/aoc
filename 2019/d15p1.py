from sys import stdin
from collections import deque
from msvcrt import getch

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

def runProgramUntilNextInput():
    global v, pc
    pc = execute(pc)
    while (v[pc] % 100 != 3 and v[pc] % 100 != 99):
        pc = execute(pc)
        
def render():
    global board, i, j, WINDOW, WIDTH, HEIGHT
    print('=========================================')
    for ii in range(i - WINDOW, i + WINDOW):
        for jj in range(j - WINDOW, j + WINDOW):
            if i != ii or j != jj:
                print(board[ii][jj], end='')
            else:
                print('D', end='')
        print()
    print('=========================================')

def update(c, response):
    global board, i, j, found
    if c == 1: ni, nj = i - 1, j
    if c == 2: ni, nj = i + 1, j
    if c == 3: ni, nj = i, j - 1
    if c == 4: ni, nj = i, j + 1
    if response == 0:
        board[ni][nj] = '#'
    elif response == 1:
        board[ni][nj] = ' '
        i, j = ni, nj
    elif response == 2:
        found = True
        board[ni][nj] = 'O'
        i, j = ni, nj
        
def left(c):
    return [-1, 3, 4, 2, 1][c]
def right(c):
    return [-1, 4, 3, 1, 2][c]

refv = [int(w) for w in input().split(',')]
v = refv[:]
v.extend((0 for _ in range(1000000)))
pc = 0
rb = 0
iq, oq = deque(), deque()

UNVISITED = 1000000000
WINDOW, WIDTH, HEIGHT = 20, 1000, 1000
# run a small state machine that implements the right-hand-on-wall 
# maze rule; preliminary probing suggests the field is maze-like with 
# single-width corridors, so this should find the target eventually
state, dir = 1, 3
found = False
board = [['.' for j in range(WIDTH)] for i in range(HEIGHT)]
ms = [[UNVISITED for j in range(WIDTH)] for i in range(HEIGHT)]
i, j = WIDTH // 2, HEIGHT // 2
board[i][j] = 'X'
ms[i][j] = 0
while not found:

    # determine next input
    if state == 1:
        c = dir
    elif state == 2:
        c = right(dir)

    iq.append(c)
    runProgramUntilNextInput()
    response = oq.popleft()

    # handle output
    if state == 1:
        if response == 0:
            dir = left(dir)
        if response == 1 or response == 2:
            state = 2
    elif state == 2:
        if response == 0:
            state = 1
        if response == 1 or response == 2:
            dir = right(dir)

    update(c, response)

    # track min steps
    if ms[i][j] == UNVISITED:
        ms[i][j] = min(ms[i - 1][j], ms[i + 1][j], ms[i][j - 1], ms[i][j + 1]) + 1

print(ms[i][j])