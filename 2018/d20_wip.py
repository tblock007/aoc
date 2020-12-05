import sys



class coord:
    def __init__(self, i, j):
        self.i, self.j = i, j

    def __str__(self):
        return '({0},{1})'.format(self.i, self.j)

    def go(self, dir, al):
        if dir == 'N':
            nex = coord(self.i - 1, self.j)
        if dir == 'E':
            nex = coord(self.i, self.j + 1)
        if dir == 'S':
            nex = coord(self.i + 1, self.j)
        if dir == 'W':
            nex = coord(self.i, self.j - 1)

        if (self.i, self.j) not in al.keys():
            al[(self.i, self.j)] = []
        if (nex.i, nex.j) not in al.keys():
            al[(nex.i, nex.j)] = []

        al[(self.i, self.j)].append((nex.i, nex.j))
        al[(nex.i, nex.j)].append((self.i, self.j))

        self.i, self.j = nex.i, nex.j


def pal(al):
    for node, neighbors in al.items():
        print('{0}: {1}'.format(str(node), ' '.join(str(n) for n in neighbors)))


def getPrefixNode(path):
    c = path[0]
    if c == 'N' or c == 'E' or c == 'S' or c == 'W':
        return (c, path[1:])
    if c == '(':
        count = 1
        for index, cc in enumerate(path[1:]):
            if cc == '(':
                count += 1
            if cc == ')':
                count -= 1
            if count == 0:
                print('splitting into {0} and {1}'.format(path[:index + 2], path[index + 2:]))
                return path[:index + 2], path[index + 2:]


# # extends all current heads by the input path
# def extendPaths(path, al, heads):

#     if not path:
#         return

#     node, newPath = getPrefixNode(path)
#     if node == 'N' or node == 'E' or node == 'S' or node == 'W':
#         for h in heads:
#             h.go(node, al)
#         extendPaths(newPath, al, heads)
#     else: # complex case
#         for h in heads:
#             extendPaths(node[1:-1], al, heads)
#         extendPaths(newPath, al, heads)
        
# r = input().rstrip()[1:-1]
# al = dict() # maps (i,j) coordinates to a list of neighbors
# heads = [coord(0, 0)]
# extendPaths(r, al, heads)

# pal(al)
# print(stop)

r = input().rstrip()[1:-1]
al = dict() # maps (i,j) coordinates to a list of neighbors

currs = [[coord(0, 0)]] # a list of stacks
for pos, c in emumerate(r):
    
    for s, stack in enumerate(currs):

        if c == 'N' or c == 'E' or c == 'S' or c == 'W':

            curr = stack[-1]
            if c == 'N':        
                nex = coord(curr.i - 1, curr.j)
            elif c == 'E':
                nex = coord(curr.i, curr.j + 1)
            elif c == 'S':
                nex = coord(curr.i + 1, curr.j)
            elif c == 'W':
                nex = coord(curr.i, curr.j - 1)

            if curr not in al.keys():
                al[curr] = []
            if nex not in al.keys():
                al[nex] = []

            al[curr].append(nex)
            al[nex].append(curr)

            currs[s][-1] = nex

        elif c == '(':
            # create a new level
            currs.append([])

        elif c == ')':
            # propagate back down to the previous level
            newcurrs = currs.pop()
            for nc in newcurrs:
                currs[-1].append(coord(nc.i, nc.j))

        elif c == '|':
            # create a new head at the current level
            levels[-1].append(coord(0, 0))

pal(al)