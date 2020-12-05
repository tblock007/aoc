from sys import stdin

def addRule(rules, line):
    config, _, result = line.split()
    surroundings = 0
    if config[0] == '#': 
        surroundings += 16
    if config[1] == '#':
        surroundings += 8
    if config[2] == '#':
        surroundings += 4
    if config[3] == '#':
        surroundings += 2
    if config[4] == '#':
        surroundings += 1

    rules[surroundings] = (1 if result == '#' else 0)

def update(env):
    return rules[16 * env[0] + 8 * env[1] + 4 * env[2] + 2 * env[3] + 1 * env[4]]

pad = 40
finalGen = 20

lines = stdin.readlines()
rules = [0 for _ in range(32)]
state = []
state.append([0] * pad + [(1 if c == '#' else 0) for c in lines[0].split()[2]] + [0] * pad)


for line in lines[2:]:
    addRule(rules, line)

for gen in range(1, finalGen + 1):
    state.append([0 for _ in range(len(state[0]))])
    for i in range(len(state[0])):
        if i <= 1:
            state[gen][i] = update([0] * (2 - i) + state[gen - 1][0:i + 3])
        elif i >= len(state[0]) - 2:
            state[gen][i] = update(state[gen - 1][i - 2:] + [0] * (i - len(state[0]) + 3))
        else:
            state[gen][i] = update(state[gen - 1][i - 2:i + 3])
    
print(sum((index - 40) for index, value in enumerate(state[finalGen]) if value == 1))

