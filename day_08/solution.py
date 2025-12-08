#!/usr/bin/env python
import sys
from math import prod


def solve(input):
    distances = {}
    for i in range(len(input)):
        cord_1 = input[i]
        (x_1, y_1, z_1) = cord_1
        for j in range(i + 1, len(input)):
            cord_2 = input[j]
            (x_2, y_2, z_2) = cord_2
            distance = ((x_1 - x_2) ** 2) + \
                ((y_1 - y_2) ** 2) + ((z_1 - z_2) ** 2)
            distances[(cord_1, cord_2)] = distance

    circuts = {}
    boxes = {}
    circut_cnt = 0
    step_cnt = 0
    part_1 = 0
    circut_1 = None

    for dist in sorted(distances, key=lambda key: distances[key]):
        (cord_1, cord_2) = dist
        circut_1 = boxes.get(cord_1, None)
        circut_2 = boxes.get(cord_2, None)

        if circut_1 == None and circut_2 != None:
            boxes[cord_1] = circut_2
            circuts[circut_2].add(cord_1)
        elif circut_1 != None and circut_2 == None:
            boxes[cord_2] = circut_1
            circuts[circut_1].add(cord_2)
        elif circut_1 == None and circut_2 == None:
            boxes[cord_2] = circut_cnt
            boxes[cord_1] = circut_cnt
            circuts[circut_cnt] = set([cord_1, cord_2])
            circut_cnt += 1
        elif circut_1 != circut_2:
            for cord in circuts[circut_2]:
                boxes[cord] = circut_1
                circuts[circut_1].add(cord)
            circuts.pop(circut_2)

        if len(circuts[boxes[cord_1]]) == len(input):
            return (part_1, cord_1[0] * cord_2[0])

        step_cnt += 1
        if step_cnt == 1000:
            part_1 = prod(
                sorted(list(map(len, circuts.values())), reverse=True)[:3])


def part_2(input):
    result = 0
    return result


def get_input():
    input_path = "./" + sys.argv[1]
    file = open(input_path)
    result = [[int(x) for x in line.split(',')] for line in file]
    result = [(line[0], line[1], line[2]) for line in result]
    return result


input = get_input()
part_1, part_2 = solve(input)
print("Part 1:", part_1)
print("Part 2:", part_2)
