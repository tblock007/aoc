def isValid(s):
    hasDouble, hasDecreasing = False, False
    for c in range(len(s) - 1):
        if s[c] == s[c + 1]:
            hasDouble = True
        if s[c] > s[c + 1]:
            hasDecreasing = True
    return hasDouble and not hasDecreasing

a, b = 278384, 824795 # player specific input
print(sum(1 for cand in range(a, b + 1) if isValid(str(cand))))