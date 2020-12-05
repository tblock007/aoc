import sys
import re

class StarField:
    def __init__(self):
        self.left, self.right, self.top, self.bottom = 1000000, -1000000, 1000000, -1000000
        self.stars = []
    def addStar(self, s):
        self.stars.append(s)
        self.left = min(self.left, s.x)
        self.right = max(self.right, s.x)
        self.top = min(self.top, s.y)
        self.bottom = max(self.bottom, s.y)
    def tick(self):
        self.left, self.right, self.top, self.bottom = 1000000, -1000000, 1000000, -1000000
        for s in self.stars:
            s.tick()
            self.left = min(self.left, s.x)
            self.right = max(self.right, s.x)
            self.top = min(self.top, s.y)
            self.bottom = max(self.bottom, s.y)


class Star:
    def __init__(self, x, y, vx, vy):
        self.x, self.y, self.vx, self.vy = x, y, vx, vy
    def tick(self):
        self.x += self.vx
        self.y += self.vy

def printstars(field, t):
    width = field.right - field.left + 1
    height = field.bottom - field.top + 1
    if width > 100 or height > 100:
        return

    print('========================')
    print('At time {0}'.format(t))
    grid = [[' ' for j in range(width)] for i in range(height)]
    for s in field.stars:
        grid[s.y - field.top][s.x - field.left] = '#'
    for row in grid:
        print(''.join(row))
    print('========================')


field = StarField()
splitter = re.compile('[^-0-9]+')
for line in sys.stdin.readlines():
    x, y, vx, vy = [int(s) for s in splitter.split(line) if len(s) > 0]
    field.addStar(Star(x, y, vx, vy))
t = 0
while True:
    field.tick()
    t += 1
    printstars(field, t)
