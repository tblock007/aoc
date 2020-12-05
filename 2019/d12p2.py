from math import gcd

def uvel(m, v):
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            if m[i] < m[j]:
                v[i] += 1
                v[j] -= 1
            elif m[i] > m[j]:
                v[i] -= 1
                v[j] += 1

def move(m, v):
    for i in range(len(m)):
        m[i] += v[i]

def findCycle(m, v):
    im, iv = m[:], v[:]
    uvel(m, v)
    move(m, v)
    count = 1
    while (im != m or iv != v):
        uvel(m, v)
        move(m, v)
        count += 1
    return count

def lcm(a, b):
    return a * b // gcd(a, b)

m = []
m.append([-15, 1, 4])
m.append([1, -10, -8])
m.append([-5, 4, 9])
m.append([4, 6, -2])
v = [[0 for c in range(3)] for i in range(len(m))]

x = findCycle([m[i][0] for i in range(len(m))], [v[i][0] for i in range(len(m))])
y = findCycle([m[i][1] for i in range(len(m))], [v[i][1] for i in range(len(m))])
z = findCycle([m[i][2] for i in range(len(m))], [v[i][2] for i in range(len(m))])
print(lcm(lcm(x, y), z))

