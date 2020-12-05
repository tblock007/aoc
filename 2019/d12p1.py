def uvel(m, v):
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            for c in range(3):
                if m[i][c] < m[j][c]:
                    v[i][c] += 1
                    v[j][c] -= 1
                elif m[i][c] > m[j][c]:
                    v[i][c] -= 1
                    v[j][c] += 1

def move(m, v):
    for i in range(len(m)):
        for c in range(3):
            m[i][c] += v[i][c]

def energy(m, v):
    e = 0
    for i in range(len(m)):
        p = abs(m[i][0]) + abs(m[i][1]) + abs(m[i][2])
        k = abs(v[i][0]) + abs(v[i][1]) + abs(v[i][2])
        e += p * k
    return e

m = []
m.append([-15, 1, 4])
m.append([1, -10, -8])
m.append([-5, 4, 9])
m.append([4, 6, -2])
v = [[0 for c in range(3)] for i in range(len(m))]

for step in range(1000):
    uvel(m, v)
    move(m, v)
print(energy(m, v))

