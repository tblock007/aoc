from sys import stdin

def total(f):
    t = 0
    while (f // 3 - 2 > 0):
        f = f // 3 - 2
        t += f
    return t

print(sum(total(int(w)) for w in stdin.readlines()))