import sys
import re
from collections import deque

def printgrid(grid):
    for row in grid:
        print(''.join(str(c) if c != 0 else ' ' for c in row))
    print()

class Source:

    parent = dict()

    def __init__(self, i, j, pi, pj):
        self.i = i
        self.j = j
        if (i, j) not in Source.parent.keys():
            Source.parent[(i, j)] = (pi, pj)


    def dropToFloor(self, grid):
        global height
        i = self.i
        while i < height - 1 and (grid[i + 1][self.j] == 0 or grid[i + 1][self.j] == 2):
            grid[i][self.j] = 2
            i += 1        
        return (i, self.j)


    def propagateAlongFloor(self, grid, sources, i, j):
        global height

        if i == height - 1:
            return False

        leftWall, rightWall = -1, -1
        l = j - 1
        while (grid[i + 1][l] == 3 or grid[i + 1][l] == 1) and (grid[i][l] == 0 or grid[i][l] == 2):
            grid[i][l] = 2
            l -= 1
        if grid[i][l] == 1:
            leftWall = l
        elif grid[i + 1][l] == 0:
            grid[i][l] = 2
            if (i, l) not in Source.parent.keys():
                sources.append(Source(i, l, self.i, self.j))
        
        r = j + 1
        while (grid[i + 1][r] == 3 or grid[i + 1][r] == 1) and (grid[i][r] == 0 or grid[i][r] == 2):
            grid[i][r] = 2
            r += 1
        if grid[i][r] == 1:
            rightWall = r
        elif grid[i + 1][r] == 0:
            grid[i][r] = 2
            if (i, r) not in Source.parent.keys():
                sources.append(Source(i, r, self.i, self.j))

        if leftWall != -1 and rightWall != -1:
            grid[i][leftWall + 1:rightWall] = [3] * (rightWall - leftWall - 1)

            p = (self.i, self.j)
            while p != (-1, -1):
                p = Source.parent[(p[0], p[1])]
                if not isComplete(grid, p[0], p[1]):
                    sources.append(Source(p[0], p[1], -1, -1))
                    break
            return True

        return False



def isComplete(grid, i, j):

    if i < 0 or j < 0:
        return True

    while i < height - 1 and (grid[i + 1][j] == 0 or grid[i + 1][j] == 2):
        grid[i][j] = 2
        i += 1

    leftWall, rightWall = -1, -1
    l = j - 1
    while (grid[i + 1][l] == 3 or grid[i + 1][l] == 1) and (grid[i][l] == 0 or grid[i][l] == 2):
        l -= 1
    if grid[i][l] == 1:
        leftWall = l
    
    r = j + 1
    while (grid[i + 1][r] == 3 or grid[i + 1][r] == 1) and (grid[i][r] == 0 or grid[i][r] == 2):
        r += 1
    if grid[i][r] == 1:
        rightWall = r

    if leftWall != -1 and rightWall != -1:
        return False
    return True




miny, maxy = 1000000000, -1000000000
offset, width, height = 480, 300, 2000

grid = [[0 for _ in range(offset, offset + width)] for _ in range(height)]
pattern = re.compile('[0-9]+')
for line in sys.stdin.readlines():
    coord, p1, p2 = [int(n) for n in pattern.findall(line)]
    if line[0] == 'x':
        miny, maxy = min(miny, p1), max(maxy, p2)
        for i in range(p1, p2 + 1):
            grid[i][coord - offset] = 1
    elif line[0] == 'y':
        miny, maxy = min(miny, coord), max(maxy, coord)
        for j in range(p1, p2 + 1):
            grid[coord][j - offset] = 1


grid[0][500 - offset] = 2
sources = deque()
sources.append(Source(0, 500 - offset, -1, -1)) # signifies no parent
while sources:
    source = sources.popleft()
    fi, fj = source.dropToFloor(grid)
    while source.propagateAlongFloor(grid, sources, fi, fj): 
        fi, fj = source.dropToFloor(grid)

count = sum(sum(1 for j in range(len(grid[i])) if grid[i][j] == 2 or grid[i][j] == 3) for i in range(miny, maxy + 1))
print(count)
