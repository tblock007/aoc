from sys import stdin

print(sum((int(w) // 3 - 2) for w in stdin.readlines()))