from sys import stdin

def instructions(line):
    instrs = line.split(',')
    return [(instr[0], int(instr[1:])) for instr in instrs]

def points(instructions):
    result = set()
    x, y = 0, 0
    for instr in instructions:
        if instr[0] == 'R':
            for xx in range(x + 1, x + instr[1]):
                result.add((xx, y))
            x += instr[1]
        elif instr[0] == 'L':
            for xx in range(x - 1, x - instr[1], -1):
                result.add((xx, y))
            x -= instr[1]
        elif instr[0] == 'U':
            for yy in range(y + 1, y + instr[1]):
                result.add((x, yy))
            y += instr[1]
        elif instr[0] == 'D':
            for yy in range(y - 1, y - instr[1], -1):
                result.add((x, yy))
            y -= instr[1]
    return result

def solve(points1, points2):
    intersections = points1.intersection(points2)
    print(min((abs(point[0]) + abs(point[1])) for point in intersections))
    
points1 = points(instructions(stdin.readline()))
points2 = points(instructions(stdin.readline()))
solve(points1, points2)