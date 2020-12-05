from sys import stdin

WIDTH, HEIGHT = 25, 6

def combine(a, b):
    if a == '2': return b
    return a

def overlay(l1, l2):
    for i in range(len(l1)):
        l1[i] = combine(l1[i], l2[i])

def convert(l):
    return ['0' if c == '1' else ' ' for c in l]
    
def output(l):
    si = 0
    while si < len(l):
        print(''.join(l[si:(si + WIDTH)]))
        si += WIDTH

s = stdin.readline().strip()
si = 0
layers = []
while si < len(s):
    layers.append(s[si:(si + WIDTH*HEIGHT)])
    si += WIDTH*HEIGHT

image = ['2' for _ in range(WIDTH*HEIGHT)]
for layer in layers:
    overlay(image, layer)
ci = convert(image)
output(ci)