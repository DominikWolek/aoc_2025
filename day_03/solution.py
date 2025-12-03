#!/usr/bin/env python
import sys


def part_1(input):
    return sum([find_largest_num(bank, 2) for bank in input])


def part_2(input):
    return sum([find_largest_num(bank, 12) for bank in input])


def find_largest_num(digits, digits_cnt):
    result = 0
    for i in range(1, digits_cnt + 1):
        num = max(digits[: len(digits) - digits_cnt + i])
        index = digits.index(num)
        bank = digits[index + 1:]
        result += num * pow(10, digits_cnt - i)
    return result


def get_input():
    input_path = "./" + sys.argv[1]
    file = open(input_path)
    result = [[int(i) for i in line.strip()] for line in file]
    return result


input = get_input()
print("Part 1:", part_1(input))
print("Part 2:", part_2(input))
