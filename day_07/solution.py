#!/usr/bin/env python
import sys


def part_1(input):
    result = 0

    input[1][input[0].index('S')] = '|'

    for i in range(2, len(input) - 1):
        beam = 0
        for _ in range(input[i - 1].count('|')):
            beam = input[i - 1][beam+1:].index('|') + beam + 1
            if input[i][beam] == '.':
                input[i][beam] = '|'
            elif input[i][beam] == '^':
                input[i][beam + 1] = '|'
                input[i][beam - 1] = '|'
                result += 1

    return result


def part_2(input):
    timelines = {}

    start = input[0].index('S')
    input[1][start] = '|'
    timelines[(1, start)] = 1

    for i in range(2, len(input) - 1):
        beam = 0
        for _ in range(input[i - 1].count('|')):
            beam = input[i - 1][beam+1:].index('|') + beam + 1
            if input[i][beam] == '^':
                timelines[(i, beam + 1)] = timelines.get((i,
                                                          beam + 1), 0) + timelines[(i - 1, beam)]
                timelines[(i, beam - 1)] = timelines.get((i,
                                                          beam - 1), 0) + timelines[(i - 1, beam)]
                input[i][beam + 1] = '|'
                input[i][beam - 1] = '|'
            else:
                input[i][beam] = '|'
                timelines[(i, beam)] = timelines.get((i,
                                                      beam), 0) + timelines[(i - 1, beam)]

    return sum(timelines.get((len(input) - 2, x), 0) for x in range(len(input[0])))


def get_input():
    input_path = "./" + sys.argv[1]
    file = open(input_path)
    result = [list(line) for line in file]
    return result


input = get_input()
print("Part 1:", part_1(list([list(line) for line in input])))
print("Part 2:", part_2(list(input)))
