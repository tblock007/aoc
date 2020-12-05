from sys import stdin

WIDTH, HEIGHT = 25, 6

def count(s, c):
    return sum(1 for char in s if char == c)

s = stdin.readline().strip()
si = 0
layers = []
while si < len(s):
    layers.append(s[si:(si + WIDTH*HEIGHT)])
    si += WIDTH*HEIGHT

minCount = WIDTH*HEIGHT+1
minIndex = -1
for index, layer in enumerate(layers):
    zeroCount = count(layer, '0')
    if zeroCount < minCount:
        minCount = zeroCount
        minIndex = index

print(count(layers[minIndex], '1') * count(layers[minIndex], '2'))