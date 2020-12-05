from sys import stdin

input = 554401
l = 6
p10 = 100000

scores = [3, 7, 1, 0, 1, 0]
a, b = 3, 4
suffix = 371010
while scores[-1 * l:] != input:
    c = scores[a] + scores[b]
    if c > 9:
        d = c // 10
        scores.append(d)
        suffix = (suffix % p10) * 10 + d
        if (suffix == input):
            break

        d = c % 10
        scores.append(d)
        suffix = (suffix % p10) * 10 + d
        if (suffix == input):
            break

    else:
        scores.append(c)
        suffix = (suffix % p10) * 10 + c
        if (suffix == input):
            break
    a = (a + 1 + scores[a]) % len(scores)
    b = (b + 1 + scores[b]) % len(scores)
    

print(len(scores) - l)