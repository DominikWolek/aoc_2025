#!/usr/bin/env python
import sys
import z3


def part_1(lights, buttons):
    result = 0

    for i in range(len(lights)):
        light = lights[i]
        zeros = tuple([0 for x in light])
        bs = buttons[i]

        conns = {zeros: (0, None)}
        q = [zeros]
        while light not in conns:
            curr_lights = q[0]
            dist = conns[curr_lights][0]
            q = q[1:]
            for button in bs:
                new_lights = add_lights(curr_lights, button)
                if new_lights not in conns:
                    conns[new_lights] = (dist + 1, curr_lights)
                    q.append(new_lights)

        result += conns[light][0]

    return result


def add_lights(lights, button):
    result = list(lights)
    for b in button:
        result[b] = (result[b] + 1) % 2
    return tuple(result)


def part_2(buttons, joltage):
    return sum([solve_one(buttons[i], joltage[i]) for i in range(len(buttons))])


def solve_one(buttons, joltage):
    solver = z3.Optimize()
    variables = []
    for b in buttons:
        var = z3.Int(str(b))
        variables.append(var)
        solver.add(var >= 0)

    for i in range(len(joltage)):
        bs = []
        for j in range(len(buttons)):
            if i in buttons[j]:
                bs.append(variables[j])
        solver.add(sum(bs) == joltage[i])

    solver.minimize(sum(variables))
    solver.check()
    model = solver.model()
    return sum([model[v].as_long() for v in variables])


def get_input():
    input_path = "./" + sys.argv[1]
    file = open(input_path)
    splitted = [line.split() for line in file]
    lights = [tuple(map(lambda x: int(x == '#'), line[0][1:-1]))
              for line in splitted]
    buttons = [list(map(lambda x: list(map(int, x[1:-1].split(','))), line[1:-1]))
               for line in splitted]

    joltage = [tuple(map(int, line[-1][1:-1].split(','))) for line in splitted]
    return lights, buttons, joltage


lights, buttons, joltage = get_input()
print("Part 1:", part_1(lights, buttons))
print("Part 2:", part_2(buttons, joltage))
