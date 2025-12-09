#!/usr/bin/env python
import sys
from shapely import Polygon


def part_1(input):
    return max([area((p_0, p_1)) for p_0 in input for p_1 in input])


def area(pair):
    (x_0, y_0) = pair[0]
    (x_1, y_1) = pair[1]
    return (abs(x_0 - x_1) + 1) * (abs(y_0 - y_1) + 1)


def part_2(input):
    poly = Polygon([[x, y] for (x, y) in input])
    contained = filter(lambda pair: poly.contains(rectangle((pair))), [
        (p_0, p_1) for p_0 in input for p_1 in input])
    return max(map(area, contained))


def rectangle(pair):
    (x_0, y_0) = pair[0]
    (x_1, y_1) = pair[1]
    return Polygon([[x_0, y_0], [x_1, y_0], [x_1, y_1], [x_0, y_1]])


def get_input():
    input_path = "./" + sys.argv[1]
    file = open(input_path)
    result = [[int(x) for x in line.split(",")] for line in file]
    result = [(line[0], line[1]) for line in result]
    return result


input = get_input()
print("Part 1:", part_1(input))
print("Part 2:", part_2(input))
