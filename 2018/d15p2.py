from sys import stdin
from collections import deque

class Unit:
    def __init__(self, i, j, c, a):
        self.c = c
        self.i = i
        self.j = j
        self.hp = 200
        self.att = a

    def __lt__(self, other):
        return (self.i < other.i) or (self.i == other.i and self.j < other.j)

    def getUnitIndex(grid, units, i, j):
        for index, unit in enumerate(units):
            if unit.i == i and unit.j == j and unit.hp > 0:
                return index
        return -1

    def takeTurn(self, grid, units):
        if self.hp <= 0:
            return -1
        self.move(grid)
        attacked = self.attack(grid, units)
        return attacked

    def move(self, grid):
        if grid[self.i - 1][self.j] == self.enemy() or grid[self.i][self.j - 1] == self.enemy() or grid[self.i][self.j + 1] == self.enemy() or grid[self.i + 1][self.j] == self.enemy():
            return

        adj = []
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if (grid[i][j] == self.enemy()):
                    for ci, cj in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
                        if grid[ci][cj] == '.':
                            adj.append((ci, cj))
        
        target = self.getClosestReachable(grid, adj)
        if target == (-1, -1):
            return

        if target[0] != self.i or target[1] != self.j:
            stepsAway = getDistances(grid, target[0], target[1])
            newSteps = [stepsAway[self.i - 1][self.j], stepsAway[self.i][self.j - 1], stepsAway[self.i][self.j + 1], stepsAway[self.i + 1][self.j]]
            bestDir = newSteps.index(min(newSteps))
            newPos = [(self.i - 1, self.j), (self.i, self.j - 1), (self.i, self.j + 1), (self.i + 1, self.j)][bestDir]
            grid[self.i][self.j] = '.'
            self.i = newPos[0]
            self.j = newPos[1]
            grid[self.i][self.j] = self.c


    def attack(self, grid, units):
        enemyIndex = self.getAdjacentEnemy(grid, units)
        if enemyIndex == -1:
            return 0
        units[enemyIndex].hp -= self.att
        if units[enemyIndex].hp <= 0:
            grid[units[enemyIndex].i][units[enemyIndex].j] = '.'
        return 1
        
    def enemy(self):
        if self.c == 'G':
            return 'E'
        else:
            return 'G'

    def getAdjacentEnemy(self, grid, units):
        hp, index = 1000000000, -1
        for candidateIndex in [Unit.getUnitIndex(grid, units, ci, cj) for ci, cj in [(self.i - 1, self.j), (self.i, self.j - 1), (self.i, self.j + 1), (self.i + 1, self.j)]]:
            if candidateIndex != -1 and units[candidateIndex].c == self.enemy():
                if units[candidateIndex].hp > 0 and units[candidateIndex].hp < hp:
                    hp, index = units[candidateIndex].hp, candidateIndex
        return index

    def getClosestReachable(self, grid, targets):
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        q = deque()
        q.append((self.i, self.j))
        visited[self.i][self.j] = True
        while q:
            curr = q.popleft()
            if curr in targets:
                return curr
            for ni, nj in [(curr[0] - 1, curr[1]), (curr[0], curr[1] - 1), (curr[0], curr[1] + 1), (curr[0] + 1, curr[1])]:
                if not visited[ni][nj] and grid[ni][nj] == '.':
                    q.append((ni, nj))
                    visited[ni][nj] = True
        return (-1, -1)


    

def printGrid(grid):
    for row in grid:
        print(''.join(c for c in row), end='')
    print()

def getDistances(grid, i, j):
    dist = [[1000000000 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    q = deque()
    q.append((i, j))
    dist[i][j] = 0
    while q:
        curr = q.popleft()
        for ni, nj in [(curr[0] - 1, curr[1]), (curr[0], curr[1] - 1), (curr[0], curr[1] + 1), (curr[0] + 1, curr[1])]:
            if dist[ni][nj] == 1000000000 and grid[ni][nj] == '.':
                q.append((ni, nj, dist[curr[0]][curr[1]] + 1))
                dist[ni][nj] = dist[curr[0]][curr[1]] + 1
    return dist

def endCombat(units):
    ec = sum(1 for unit in units if unit.hp > 0 and unit.c == 'E')
    gc = sum(1 for unit in units if unit.hp > 0 and unit.c == 'G')
    if ec == 0:
        return ('E', True)
    elif gc == 0:
        return ('G', True)
    else:
        return ('?', False)

def getTotalHP(units):
    return sum(unit.hp for unit in units if unit.hp > 0)

def countElves(units):
    return sum(1 for unit in units if unit.c == 'E' and unit.hp > 0)

def simulate(inp, a):   
    grid = []
    units = []
    for i, line in enumerate(inp):
        gridRow = []
        for j, c in enumerate(line):
            if c == 'G' or c == 'E':
                units.append(Unit(i, j, c, (a if c == 'E' else 3)))
            gridRow.append(c)
        grid.append(gridRow)

    initialElfCount = countElves(units)

    round = 0
    while True:
        winner, end = endCombat(units)
        if end:
            break
        
        lastAction = -1
        units.sort()
        for unit in units:
            acted = unit.takeTurn(grid, units)
            if acted != -1:
                lastAction = acted

        if countElves(units) != initialElfCount:
            print('Elf died when attack power is {0}!  There are now {1} elves.'.format(a, countElves(units)))
            return
        
        round += 1        
        # print('{0} ======================='.format(round))
        # printGrid(grid)
        # for unit in units:
        #     print('units at {0},{1} has {2} HP'.format(unit.i, unit.j, unit.hp))
        # print('{0} ======================='.format(round))

    if lastAction == 0:
        round -= 1
    print('No elf deaths when attack power is {0}!  Round outcome is {1}'.format(a, getTotalHP(units) * round))


# Manually checking elf power to determine minimum power that results in simulate returning True
lines = stdin.readlines()
simulate(lines, 13)
simulate(lines, 14)