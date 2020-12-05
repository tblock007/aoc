from sys import stdin

def readNode(seq, i):
    children, meta = seq[i], seq[i + 1]
    numRead = 2

    value = 0
    if children == 0:
        for m in range(meta):
            value += seq[i + numRead]
            numRead += 1
    else:
        childrenValues = [0 for _ in range(children)]
        for c in range(children):
            childrenValues[c], additionalRead = readNode(seq, i + numRead)
            numRead += additionalRead
        for m in range(meta):
            index = seq[i + numRead] - 1
            numRead += 1
            if index >= 0 and index < children:
                value += childrenValues[index]
    
    return (value, numRead)


seq = [int(w) for w in input().split()]
value, _ = readNode(seq, 0)
print(value)