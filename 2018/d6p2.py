from sys import stdin
from collections import deque

class Coord:
    def __init__(self, i, j):
        self.i = i
        self.j = j 

def ff(i, j, newVal):
    ffq = deque()
    ffq.append(Coord(i, j))
    distance[i][j] = newVal
    result = 1

    while ffq:
        curr = ffq.popleft()
        for d in range(len(dr)):
            ni, nj = curr.i + dr[d], curr.j + dc[d]
            if ni >= 0 and ni < n and nj >= 0 and nj < n:
                if distance[ni][nj] < threshold:
                    ffq.append(Coord(ni, nj))
                    distance[ni][nj] = newVal
                    result += 1

    return result

n = 400
threshold = 10000
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

# init BFS
distance = [[0 for i in range(n)] for j in range(n)]
for line in stdin.readlines():
    y = int(line.split(',')[0].strip())
    x = int(line.split(',')[1].strip())
    for i in range(n):
        for j in range(n):
            distance[i][j] += (abs(i - x) + abs(j - y))

# flood fill count based on distance threshold and return max
maxArea = -1
for i in range(n):
    for j in range(n):
        if distance[i][j] < threshold:
            area = ff(i, j, threshold + 1)
            maxArea = max(maxArea, area)
print(maxArea)