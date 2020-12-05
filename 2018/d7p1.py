from sys import stdin

steps = 26

def getFirstFree():
    for index, dep in enumerate(deps):
        if dep == 0:
            deps[index] = -1
            return index

deps = [0 for i in range(steps)]
al = [[] for i in range(steps)]
for line in stdin.readlines():
    pre, post = ord(line[5]) - ord('A'), ord(line[36]) - ord('A')
    deps[post] += 1
    al[pre].append(post)

result = ''
while len(result) < steps:
    free = getFirstFree()
    result += chr(free + ord('A'))
    for nex in al[free]:
        deps[nex] -= 1
print(result)
