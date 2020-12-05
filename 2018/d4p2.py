import sys
import re

lines = sorted(sys.stdin.readlines())
splitter = re.compile('[\D]+')
asleep = [[] for i in range(60)]
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
        for mm in range(sleepStart, sleepEnd):
            asleep[mm].append(guard)

bestGuard, bestCount, bestMinute = -1, -1, -1
for mm in range(60):
    if len(asleep[mm]) > 0:
        bestGuardMinute = max(asleep[mm], key = asleep[mm].count)
        bestCountMinute = asleep[mm].count(bestGuardMinute)
        if (bestCountMinute > bestCount):
            bestCount, bestGuard, bestMinute = bestCountMinute, bestGuardMinute, mm
print(bestGuard, bestCount, mm, bestGuard * bestMinute)



    
