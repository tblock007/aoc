from sys import stdin

class resultHolder:
    def __init__(self):
        self.x = 0
    def add(self, n):
        self.x += n

def readNode(seq, i, result):
    children, meta = seq[i], seq[i + 1]
    numRead = 2
    for c in range(children):
        numRead += readNode(seq, i + numRead, result)
    for m in range(meta):
        result.add(seq[i + numRead])
        numRead += 1
    return numRead


seq = [int(w) for w in input().split()]
result = resultHolder()
readNode(seq, 0, result)
print(result.x)