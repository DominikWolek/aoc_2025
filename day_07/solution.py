#!/usr/bin/env python
import sys


def part_1(input):
    result = 0

    curr = set()
    curr.add(input[0].index('S'))
    next = set()

    for i in range(1, len(input)):
        for beam in curr:
            if input[i][beam] == '^':
                next.add(beam - 1)
                next.add(beam + 1)
                result += 1
            else:
                next.add(beam)

        curr = next
        next = set()

    return result


def part_2(input):
    timelines = {}

    curr = {input[0].index('S'): 1}
    next = {}

    for i in range(1, len(input)):
        for beam in curr.keys():
            if input[i][beam] == '^':
                next[beam + 1] = next.get(beam + 1, 0) + curr[beam]
                next[beam - 1] = next.get(beam - 1, 0) + curr[beam]
            else:
                next[beam] = next.get(beam, 0) + curr[beam]

        curr = next
        next = {}

    return sum(curr.values())


def get_input():
    input_path = "./" + sys.argv[1]
    file = open(input_path)
    result = [list(line) for line in file]
    return result


input = get_input()
print("Part 1:", part_1(input))
print("Part 2:", part_2(list(input)))
