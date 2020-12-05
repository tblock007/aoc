import sys
ids = sys.stdin.readlines()
patterns = set()
for id in ids:
    for i in range(len(id)):
        pattern = id[0:i] + '?' + id[i+1:]
        if pattern in patterns:
            print(''.join(c for c in pattern if c != '?'))
        patterns.add(pattern)
