def isValid(i):
    s = '-' + str(i) + '-'
    hasDouble, hasDecreasing = False, False
    for c in range(1, len(s) - 2):
        if s[c] == s[c + 1]:
            if (s[c - 1] != s[c] and s[c + 2] != s[c]):
                hasDouble = True
        if s[c] > s[c + 1]:
            hasDecreasing = True
    return hasDouble and not hasDecreasing

a, b = 278384, 824795 # player specific input
print(sum(1 for cand in range(a, b + 1) if isValid(cand)))