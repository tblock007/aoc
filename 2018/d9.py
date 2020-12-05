class Node:
    def __init__(self, v):
        self.val = v
        self.prev = None
        self.next = None

def place(x):
    global curr
    result = 0
    if x % 23 == 0:
        for _ in range(7):
            curr = curr.prev
        result += (x + curr.val)
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr = curr.next
    else:
        curr = curr.next.next
        tbi = Node(x)
        curr.prev.next, tbi.prev = tbi, curr.prev
        curr.prev, tbi.next = tbi, curr
        curr = tbi
    return result


players = 459
nm = 71320 # for part 1
# nm = 7132000 # for part 2

scores = [0 for _ in range(players)]
curr = Node(0)
curr.prev, curr.next = curr, curr

x = 1
while x < nm:
    scores[(x - 1) % players] += place(x)
    x += 1

print(max(scores))