#!/usr/bin/env python
import sys


def part_1(input):
    result = 0
    start = 50
    for (direction, num) in input:
        if direction == 'L':
            start -= num
        elif direction == 'R':
            start += num
        start = start % 100
        if start == 0:
            result += 1
    return result


def part_2(input):
    result = 0
    start = 50
    for (direction, num) in input:
        for i in range (0, num):
            if direction == 'L':
                start -= 1
            elif direction == 'R':
                start += 1
            start = start % 100
            if start == 0:
                result += 1
    return result


def get_input():
    input_path = "./" + sys.argv[1]
    file = open(input_path)
    result = [(line[0], int(line[1:])) for line in file]
    return result


input = get_input()
print("Part 1:", part_1(input))
print("Part 2:", part_2(input))