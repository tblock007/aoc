import sys
lines = sys.stdin.readlines()
seen = set([0])
freq, found = 0, False
while not found:
    for line in lines:
        freq += int(line)
        if freq in seen:
            print(freq)
            found = True
            break
        seen.add(freq)
