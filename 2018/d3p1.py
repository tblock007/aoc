import sys
import re

fabric = [[0 for j in range(1000)] for i in range(1000)]

splitter = re.compile('[\D]+')
for line in sys.stdin.readlines():
    index, a, b, w, h = [int(s) for s in splitter.split(line) if len(s) > 0]
    for i in range(b, b + h):
        for j in range(a, a + w):
            fabric[i][j] += 1

count = sum(sum((1 if fabric[i][j] > 1 else 0) for j in range(1000)) for i in range(1000))
