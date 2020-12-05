import sys
import re

lines = sys.stdin.readlines()
fabric = [[0 for j in range(1000)] for i in range(1000)]

splitter = re.compile('[\D]+')
for line in lines:
    index, a, b, w, h = [int(s) for s in splitter.split(line) if len(s) > 0]
    for i in range(b, b + h):
        for j in range(a, a + w):
            if fabric[i][j] != 0:
                fabric[i][j] = -1
            else:
                fabric[i][j] = index

for line in lines:    
    index, a, b, w, h = [int(s) for s in splitter.split(line) if len(s) > 0]
    conflict = False
    for i in range(b, b + h):
        for j in range(a, a + w):
            if fabric[i][j] != index:
                conflict = True
    if not conflict:
        print(index)
        break
