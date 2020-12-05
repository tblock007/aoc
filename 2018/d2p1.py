def getCounts(s):
    counts = [0 for _ in range(26)]
    for c in s:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            counts[ord(c) - ord('a')] += 1
    return counts

def containsN(counts, n):
    for count in counts:
        if count == n:
            return True
    return False


import sys
ids = sys.stdin.readlines()
c2, c3 = 0, 0
for id in ids:
    idCounts = getCounts(id)
    if (containsN(idCounts, 2)):
        c2 += 1
    if (containsN(idCounts, 3)):
        c3 += 1
print(c2 * c3)
