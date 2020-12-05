def powerLevel(x, y, serial):
    rid = x + 10
    p = rid * y
    p += serial
    p *= rid
    p = (p // 100) % 10
    return (p - 5)

def sumRegion(grid, i0, j0):
    return sum(sum(grid[i0 + i][j0 + j] for j in range(3)) for i in range(3))

s = 8979
grid = [[powerLevel(x, y, s) for x in range(1, 301)] for y in range(1, 301)]
best = -100
besti, bestj = -1, -1
for i0 in range(300 - 2):
    for j0 in range(300 - 2):
        r = sumRegion(grid, i0, j0)
        if r > best:
            best = r
            besti, bestj = i0, j0

print(bestj + 1, besti + 1)

