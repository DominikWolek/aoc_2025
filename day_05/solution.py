#!/usr/bin/env python
import sys


def part_1(ranges, ids):
    return len(list(filter(lambda id: any([does_fit(id, r) for r in ranges]), ids)))


def does_fit(id, range):
    (left, right) = range
    return id >= left and id <= right


def part_2(ranges):
    ranges.sort()
    final = [ranges[0]]

    for (left, right) in ranges[1:]:
        (last_left, last_right) = final[-1]
        if (left > last_right):
            final.append((left, right))
        else:
            final[-1] = (min(left, last_left), max(right, last_right))

    return sum(map(lambda range: range[1] - range[0] + 1, final))


def get_input():
    input_path = "./" + sys.argv[1]
    file = open(input_path)
    ranges = []
    ids = []
    for line in file:
        if line != "\n":
            if line.find('-') != -1:
                splitted = line.split('-')
                ranges.append((int(splitted[0]), int(splitted[1])))
            else:
                ids.append(int(line))
    return (ranges, ids)


(ranges, ids) = get_input()
print("Part 1:", part_1(ranges, ids))
print("Part 2:", part_2(ranges))
