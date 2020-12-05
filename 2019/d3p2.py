from sys import stdin

def instructions(line):
    instrs = line.split(',')
    return [(instr[0], int(instr[1:])) for instr in instrs]

def points(instructions):
    result = set()
    timeReached = dict()
    x, y, steps = 0, 0, 0
    for instr in instructions:
        if instr[0] == 'R':
            for xx in range(1, instr[1] + 1):
                steps += 1
                result.add((x + xx, y))
                if (x + xx, y) not in timeReached.keys():
                    timeReached[(x + xx, y)] = steps
            x += instr[1]
        elif instr[0] == 'L':
            for xx in range(-1, -instr[1] - 1, -1):
                steps += 1
                result.add((x + xx, y))
                if (x + xx, y) not in timeReached.keys():
                    timeReached[(x + xx, y)] = steps
            x -= instr[1]
        elif instr[0] == 'U':
            for yy in range(1, instr[1] + 1):
                steps += 1
                result.add((x, y + yy))
                if (x, y + yy) not in timeReached.keys():
                    timeReached[(x, y + yy)] = steps
            y += instr[1]
        elif instr[0] == 'D':
            for yy in range(-1, -instr[1] - 1, -1):
                steps += 1
                result.add((x, y + yy))
                if (x, y + yy) not in timeReached.keys():
                    timeReached[(x, y + yy)] = steps
            y -= instr[1]
    return result, timeReached

def solve(points1, points2, timeReached1, timeReached2):
    intersections = points1.intersection(points2)
    print(min((timeReached1[point] + timeReached2[point]) for point in intersections))
    
points1, timeReached1 = points(instructions(stdin.readline()))
points2, timeReached2 = points(instructions(stdin.readline()))
solve(points1, points2, timeReached1, timeReached2)