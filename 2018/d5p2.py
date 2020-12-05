def isMatch(c1, c2):
    return (abs(ord(c1) - ord(c2)) == 32) # difference between 'A' and 'a'

def reducedLength(polymer, igOrdUpper):
    stack = []
    for c in polymer:
        if c != chr(igOrdUpper) and c != chr(igOrdUpper + 32):
            if len(stack) == 0 or not isMatch(stack[-1], c):
                stack.append(c)
            else:
                stack.pop()
    return len(stack)

polymer = input()
result = min(reducedLength(polymer, ignored) for ignored in range(65, 91))
print(result)
