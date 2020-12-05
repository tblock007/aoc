import sys

def printgrid(grid):
    for row in grid:
        print(''.join(str(c) for c in row))
    print()

def score(grid):
    t, l = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '|':
                t += 1
            if grid[i][j] == '#':
                l += 1
    return (t * l)

def countAdj(grid, i, j):
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    openCount, treeCount, lumberCount = 0, 0, 0
    for d in range(len(dr)):
        if i + dr[d] >= 0 and i + dr[d] < len(grid) and j + dc[d] >= 0 and j + dc[d] < len(grid[i]):
            if grid[i + dr[d]][j + dc[d]] == '.':
                openCount += 1
            if grid[i + dr[d]][j + dc[d]] == '|':
                treeCount += 1
            if grid[i + dr[d]][j + dc[d]] == '#':
                lumberCount += 1
    return (openCount, treeCount, lumberCount)

def tick(grid, i, j):
    o, t, l = countAdj(grid, i, j)
    if grid[i][j] == '.':
        if t >= 3:
            return '|'
        else:
            return '.'
    elif grid[i][j] == '|':
        if l >= 3:
            return '#'
        else:
            return '|'
    elif grid[i][j] == '#':
        if l >= 1 and t >= 1:
            return '#'
        else:
            return '.'

def update(grid):
    return [[tick(grid, i, j) for j in range(len(grid[i]))] for i in range(len(grid))]


grid = [[c for c in row.rstrip()] for row in sys.stdin.readlines()]
for _ in range(10):
    grid = update(grid)

print(score(grid))
