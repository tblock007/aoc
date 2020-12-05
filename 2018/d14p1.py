from sys import stdin

input = 554401

scores = [3, 7]
a, b = 0, 1
while len(scores) < (input + 15):
    c = scores[a] + scores[b]
    if c > 9:
        scores.append(c // 10)
        scores.append(c % 10)
    else:
        scores.append(c)
    a = (a + 1 + scores[a]) % len(scores)
    b = (b + 1 + scores[b]) % len(scores)
    

print(''.join(str(c) for c in scores[input:input + 10]))