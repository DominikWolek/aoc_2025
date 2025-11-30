#!/usr/bin/env python
import sys


def part_1(input):
    result = 0
    return result


def part_2(input):
    result = 0
    return result


def get_input():
    input_path = "./" + sys.argv[1]
    file = open(input_path)
    result = [line for line in file]
    return result


input = get_input()
print("Part 1:", part_1(input))
print("Part 2:", part_2(input))