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

def runProgramUntilNextInput():
    global v, pc
    pc = execute(pc)
    while (v[pc] % 100 != 3 and v[pc] % 100 != 99):
        pc = execute(pc)

def display(c):
    glyphs = [' ', '/', '#', '^', 'O']
    return glyphs[c]

def blocksRemaining(board):
    count = 0
    for i in range(23):
        for j in range(43):
            if board[i][j] == 2:
                count += 1
    return count

def getPositions(board):
    ballx, bally, paddley = -1, -1, -1
    for i in range(23):
        for j in range(43):
            if board[i][j] == 3:
                paddley = j
            if board[i][j] == 4:
                ballx, bally = i, j
    return (ballx, bally, paddley)

def getMove(board, ballx, bally, prevballx, prevbally, paddley):
    if paddley != bally:
        return 0
    else:
        nextballx = ballx + (ballx - prevballx)
        nextbally = bally + (bally - prevbally)
        if (board[ballx][nextbally] == 1 or board[ballx][nextbally] == 2):
            if (board[nextballx][bally] == 0 and board[ballx][prevbally] == 0 and board[nextballx][prevbally] == 2):
                if (board[prevballx][nextbally] == 1 or board[prevballx][nextbally] == 2):
                    return -(bally - prevbally)
                else:                
                    return (bally - prevbally)
            else:
                return -(bally - prevbally)
        if (board[nextballx][bally] == 1):
            if (board[prevballx][nextbally] == 1 or board[prevballx][nextbally] == 2):
                return -(bally - prevbally)
            else:
                return (bally - prevbally)
        if (board[nextballx][bally] == 2):
            if (board[prevballx][nextbally] == 1 or board[prevballx][nextbally] == 2):
                if (board[nextballx][prevbally] == 1 or board[nextballx][prevbally] == 2):
                    return (bally - prevbally)
                else:
                    return -(bally - prevbally)
            else:
                return (bally - prevbally)
        if (board[nextballx][nextbally] == 1 or board[nextballx][nextbally] == 2) and (board[nextballx][bally] != 1 and board[nextballx][bally] != 2):
            return -(bally - prevbally)
        return (bally - prevbally)   



def analyzeBoard(board):
    blocks, ballx, bally, scoreUpdate = 0, -1, -1, 0
    while oq:
        y = oq.popleft()
        x = oq.popleft()
        t = oq.popleft()
        if t == 4:
            ballx = x
            bally = y
        if x == 0 and y == -1:
            scoreUpdate = t
        else:
            board[x][y] = t
    return (blocksRemaining(board), ballx, bally, score)

def render(board, score):
    print('Score: {0}'.format(score))    
    for i in range(len(board)):
        print(''.join(display(c) for c in board[i]))
        
refv = [int(w) for w in stdin.readline().split(',')]
v = refv[:]
v.extend((0 for _ in range(1000000)))
pc = 0
rb = 0
iq, oq = deque(), deque()

v[0] = 2
board = [[0 for j in range(43)] for i in range(23)]

ballx, bally, paddley = 17, 18, 21
prevballx, prevbally = ballx - 1, bally - 1 # ball is initially traveling down-right
blocks, score = 1, 0
while blocks > 0:
    move = getMove(board, ballx, bally, prevballx, prevbally, paddley)
    iq.append(move)
    paddley += move
    runProgramUntilNextInput()
    prevballx, prevbally = ballx, bally
    blocks, ballx, bally, score = analyzeBoard(board)
runProgramUntilNextInput()