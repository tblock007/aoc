import sys
import re

def keyWithMaxVal(d):
     v = list(d.values())
     k = list(d.keys())
     return k[v.index(max(v))]



lines = sorted(sys.stdin.readlines())
splitter = re.compile('[\D]+')
totals, minutes = dict(), dict()
for line in lines:
    ints = [int(s) for s in splitter.split(line) if len(s) > 0]
    y, mo, d, h, m = ints[0:5]
    garbage, message = line.split(']')
    if message.endswith('shift\n'):
        guard = ints[5]
    elif message.endswith('asleep\n'):
        sleepStart = m
    elif message.endswith('up\n'):
        sleepEnd = m
        if guard not in totals:
            totals[guard] = 0
            minutes[guard] = [0 for _ in range(60)]
        for mm in range(sleepStart, sleepEnd):
            totals[guard] += 1
            minutes[guard][mm] += 1

chosenGuard = keyWithMaxVal(totals)
chosenMinute = minutes[chosenGuard].index(max(minutes[chosenGuard]))
print(chosenGuard, chosenMinute, chosenGuard * chosenMinute)


    
