from sys import stdin
from math import atan2, pi, sqrt

class Direction:
    def __init__(self, dx, dy):
        if dx == 0:
            self.dx, self.dy = 0, 1 if dy > 0 else -1
        elif dy == 0:
            self.dx, self.dy = 1 if dx > 0 else -1, 0
        else:
            div = gcd(dx, dy)
            self.dx = dx // div
            self.dy = dy // div
    def __eq__(self, other):
        return (self.dx == other.dx and self.dy == other.dy)
    def __hash__(self):
        return hash((self.dx, self.dy))
    def __str__(self):
        return '({0},{1})'.format(self.dx, self.dy)

def angle(p):
    global x, y
    theta = atan2(-p[1], -p[0])
    if theta < 0.0:
        theta += 2 * pi
    return theta

def dist(p):
    global x, y
    return (p[0] * p[0] + p[1] * p[1])

def vaporize(a, curr):
    theta = angle(a[curr])
    del a[curr]
    if (len(a) == 1):
        return 0
    if (curr >= len(a)):
        curr = 0
    while angle(a[curr]) == theta:
        curr += 1
        if (curr >= len(a)):
            curr = 0
    return curr

x, y = 31, 25
a = []
g = [[c for c in line.strip()] for line in stdin.readlines()]
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == '#' and not (i == x and j == y):
            a.append((i - x, -(j - y))) # this flip makes the laser go ccw

a.sort(key = lambda p : (angle(p), dist(p)))
curr = 0
for i in range(200):
    lastVaporized = (a[curr][0] + x) + (y - a[curr][1]) * 100
    curr = vaporize(a, curr)
print(lastVaporized)
