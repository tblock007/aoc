from sys import stdin

class Cart:
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1] # 0, 1, 2, 3 is up, right, down, left
    dd = [-1, 0, 1]
    
    def __init__(self, i, j, dir):
        self.nextTurn = 0
        self.i = i
        self.j = j
        self.dir = dir

    def __lt__(self, other):
        return (self.i < other.i) or (self.i == other.i and self.j < other.j)

    def tick(self, grid, crashed):
        if (self.i, self.j) in crashed:
            return
        self.i += Cart.dr[self.dir]
        self.j += Cart.dc[self.dir]
        if grid[self.i][self.j] == '/':
            self.dir = [1, 0, 3, 2][self.dir]
        elif grid[self.i][self.j] == '\\':            
            self.dir = [3, 2, 1, 0][self.dir]
        elif grid[self.i][self.j] == '+':
            self.dir = (self.dir + Cart.dd[self.nextTurn]) % len(Cart.dr)
            self.nextTurn = (self.nextTurn + 1) % len(Cart.dd)
          

def tick(grid, carts):
    carts.sort()
    crashed = set()
    for cart in carts:
        cart.tick(grid, crashed)
        if (cart.i, cart.j) in [(c.i, c.j) for c in carts if c is not cart]:
            crashed.add((cart.i, cart.j))
    carts[:] = [uncrashed for uncrashed in carts if (uncrashed.i, uncrashed.j) not in crashed]
    if len(carts) == 1:
        return False
    return True

grid = []
carts = []
for i, line in enumerate(stdin.readlines()):
    gridRow = []
    cartsRow = []
    for j, c in enumerate(line):
        if c == '^':
            gridRow.append('|')
            carts.append(Cart(i, j, 0))
        elif c == '>':
            gridRow.append('-')
            carts.append(Cart(i, j, 1))
        elif c == 'v':
            gridRow.append('|')
            carts.append(Cart(i, j, 2))
        elif c == '<':
            gridRow.append('-')
            carts.append(Cart(i, j, 3))
        else:
            gridRow.append(c)
    grid.append(gridRow)

while (tick(grid, carts)):
    pass

print(carts[0].j, carts[0].i)