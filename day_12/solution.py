#!/usr/bin/env python
import sys


def part_1(regions):
    return len(list(filter(does_fit, regions)))


def does_fit(region):
    (size, ps) = region
    return sum(ps) * 9 <= size[0] * size[1]


def part_2():
    return "Happy Holidays!"


def get_input():
    input_path = "./" + sys.argv[1]
    file = open(input_path)
    lines = [line for line in file]
    regions = list(map(lambda l: l.split(':'), lines[30:]))
    regions = [(tuple(map(int, r[0].split('x'))), list(map(int, r[1].split())))
               for r in regions]
    return regions


regions = get_input()
print("Part 1:", part_1(regions))
print("Part 2:", part_2())
