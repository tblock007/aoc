from sys import stdin

def readNode():
    global seq, i, result
    children, meta = seq[i], seq[i + 1]
    i += 2

    value = 0
    if children == 0:
        for m in range(meta):
            value += seq[i]
            i += 1
    else:
        childrenValues = [readNode() for _ in range(children)]        
        for m in range(meta):
            index = seq[i] - 1
            i += 1
            if index >= 0 and index < children:
                value += childrenValues[index]
    return value
    


seq = [int(w) for w in input().split()]
i = 0
print(readNode())