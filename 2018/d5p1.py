def isMatch(c1, c2):
    return (abs(ord(c1) - ord(c2)) == 32) # difference between 'A' and 'a'

polymer = input()
stack = []
for c in polymer:
    if len(stack) == 0 or not isMatch(stack[-1], c):
        stack.append(c)
    else:
        stack.pop()
print(len(stack))
