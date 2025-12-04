#!/usr/bin/env python
import sys
import itertools


def part_1(input):
    result = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            if accessable(input, x, y):
                result += 1
    return result


def part_2(input):
    result = 0
    while (True):
        cnt = 0
        new_input = [list(line) for line in input]
        for y in range(len(input)):
            for x in range(len(input[y])):
                if accessable(input, x, y):
                    new_input[y][x] = 'x'
                    cnt += 1
                    result += 1
        input = new_input
        if cnt == 0:
            return result


def accessable(input, x, y):
    return input[y][x] == '@' and paper_neighbours(input, x, y) < 4


dirs = [(-1, -1), (0, -1), (-1, 0), (1, -1), (-1, 1), (1, 1), (1, 0), (0, 1)]


def paper_neighbours(input, x, y):
    result = 0
    for (x_dir, y_dir) in dirs:
        (new_x, new_y) = (x + x_dir, y + y_dir)
        if new_y >= 0 and new_y < len(input) and new_x >= 0 and new_x < len(input[new_y]) and input[new_y][new_x] == '@':
            result += 1

    return result


def get_input():
    input_path = "./" + sys.argv[1]
    file = open(input_path)
    result = [line for line in file]
    return result


input = get_input()
print("Part 1:", part_1(input))
print("Part 2:", part_2(input))
