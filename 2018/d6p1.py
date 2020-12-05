from sys import stdin
from collections import deque

class Coord:
    def __init__(self, i, j):
        self.i = i
        self.j = j 

def ff(i, j, val, newVal):
    ffq = deque()
    ffq.append(Coord(i, j))
    claimed[i][j] = newVal
    result = 1

    while ffq:
        curr = ffq.popleft()
        for d in range(len(dr)):
            ni, nj = curr.i + dr[d], curr.j + dc[d]
            if ni >= 0 and ni < n and nj >= 0 and nj < n:
                if claimed[ni][nj] == val:
                    ffq.append(Coord(ni, nj))
                    claimed[ni][nj] = newVal
                    result += 1

    return result

n = 400
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

# init BFS
claimed = [[-1 for i in range(n)] for j in range(n)]
level = [[-1 for i in range(n)] for j in range(n)]
q = deque()
for index, line in enumerate(stdin.readlines()):
    j = int(line.split(',')[0].strip())
    i = int(line.split(',')[1].strip())
    claimed[i][j] = index
    level[i][j] = 0
    q.append(Coord(i, j))

# perform BFS
while q:
    curr = q.popleft()
    currLevel = level[curr.i][curr.j]

    for d in range(len(dr)):
        ni, nj = curr.i + dr[d], curr.j + dc[d]
        if ni >= 0 and ni < n and nj >= 0 and nj < n:
            if level[ni][nj] == -1:
                claimed[ni][nj] = claimed[curr.i][curr.j]
                level[ni][nj] = currLevel + 1
                q.append(Coord(ni, nj))
            elif level[ni][nj] == currLevel + 1 and not claimed[ni][nj] == claimed[curr.i][curr.j]:
                claimed[ni][nj] = -2

# flood fill edges to be invalid to cover infinite areas
for j in range(n):
    if claimed[0][j] >= 0:
        ff(0, j, claimed[0][j], -3)
    if claimed[n - 1][j] >= 0:
        ff(n - 1, j, claimed[n - 1][j], -3)
for i in range(n):
    if claimed[i][0] >= 0:
        ff(i, 0, claimed[i][0], -3)
    if claimed[i][n - 1] >= 0:
        ff(i, n - 1, claimed[i][n - 1], -3)


# flood fill count remaining and return max
maxArea = -1
for i in range(n):
    for j in range(n):
        if claimed[i][j] >= 0:
            area = ff(i, j, claimed[i][j], -3)
            maxArea = max(maxArea, area)
print(maxArea)