from sys import stdin

def readNode():
    global seq, i, result
    children, meta = seq[i], seq[i + 1]
    i += 2
    for c in range(children):
        readNode()
    for m in range(meta):
        result += seq[i]
        i += 1


seq = [int(w) for w in input().split()]
i, result = 0, 0
readNode()
print(result)