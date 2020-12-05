from sys import stdin
from math import gcd

# A Direction basically represents an angle
# __hash__ and __eq__ are supplied so that 
# two asteroids that are in the same direction
# yield the same Direction
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

a = []
g = [[c for c in line.strip()] for line in stdin.readlines()]
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == '#':
            a.append((i, j))

m = -1
x, y = -1, -1
for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == '#':
            # For every asteroid, check all other asteroids and 
            # accumulate the unique Directions in a set
            clos = set()
            for ii in range(len(g)):
                for jj in range(len(g[i])):
                    if (ii, jj) != (i, j) and g[ii][jj] == '#':
                        clos.add(Direction(ii - i, jj - j))
            if len(clos) > m:
                m, x, y = len(clos), i, j

print(m)
print(x, y)