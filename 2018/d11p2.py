def powerLevel(i, j, serial):
    x = j + 1
    y = i + 1
    rid = x + 10
    p = rid * y
    p += serial
    p *= rid
    p = (p // 100) % 10
    return (p - 5)

def sumRegion(cGrid, i, j, dim):
    bi, bj = i + dim - 1, j + dim - 1
    si, sj = i - 1, j - 1
    result = cGrid[bi][bj]
    if sj >= 0:
        result -= cGrid[bi][sj]
    if si >= 0:
        result -= cGrid[si][bj]
    if si >= 0 and sj >= 0:
        result += cGrid[si][sj]
    return result

s = 8979
cGrid = [[0 for x in range(1, 301)] for y in range(1, 301)]
cGrid[0][0] = powerLevel(0, 0, s)
for i in range(1, 300):
    cGrid[i][0] = cGrid[i - 1][0] + powerLevel(i, 0, s)
    cGrid[0][i] = cGrid[0][i - 1] + powerLevel(0, i, s)
for i in range(1, 300):
    for j in range(1, 300):
        cGrid[i][j] = cGrid[i - 1][j] + cGrid[i][j - 1] - cGrid[i - 1][j - 1] + powerLevel(i, j, s)

best = -1000000000
mi, mj, mdim = -1, -1, -1
for dim in range(1, 300):
    for i in range(300 - dim + 1):
        for j in range(300 - dim + 1):
            candidate = sumRegion(cGrid, i, j, dim)
            if candidate > best:
                best = candidate
                mi, mj, mdim = i, j, dim
print(mj + 1, mi + 1, mdim)

