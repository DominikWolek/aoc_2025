#!/usr/bin/env python
import sys


def part_1(input):
    result = 0
    for (left, right) in input:
        for i in range(left, right + 1):
            check = str(i)
            if do_check(check, 2):
                result += i
    return result


def part_2(input):
    result = 0
    for (left, right) in input:
        for i in range(left, right + 1):
            if check_repetitions(i):
                result += i

    return result


def check_repetitions(id):
    check = str(id)
    return any([do_check(check, div) for div in range(2, len(check) + 1)])


def do_check(id, div):
    length = len(id)
    if length % div == 0:
        devided = length // div
        parts = [id[i * devided : (i + 1) * devided] for i in range(div)]
        if all(part == parts[0] for part in parts):
            return True
    return False


def get_input():
    input_path = "./" + sys.argv[1]
    file = open(input_path)

    result = file.read().split(',')
    result = [r.split('-') for r in result]
    result = [(int(r[0]), int(r[1])) for r in result]
    return result


input = get_input()
print("Part 1:", part_1(input))
print("Part 2:", part_2(input))