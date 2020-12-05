from collections import deque

def place(x):
    global marbles
    result = 0
    if x % 23 == 0:
        marbles.rotate(7)
        result += (x + marbles.pop())
        marbles.rotate(-1)
    else:
        marbles.rotate(-1)
        marbles.append(x)
    return result


players = 459
nm = 71320 # for part 1
nm = 7132000 # for part 2

scores = [0 for _ in range(players)]
marbles = deque()
marbles.append(0)

x = 1
while x < nm:
    scores[(x - 1) % players] += place(x)
    x += 1

print(max(scores))