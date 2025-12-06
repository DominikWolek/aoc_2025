#!/usr/bin/env python
import sys
from math import prod


def part_1(columns, ops):
    return sum(map(lambda i: do_calc(columns[i], ops[i]), range(len(ops))))


def do_calc(nums, op):
    nums = map(int, nums)
    if op == '*':
        return prod(nums)
    else:
        return sum(nums)


def part_2(nums, ops):
    return part_1(list(map(cephalopod, nums)), ops)


def cephalopod(nums):
    new_nums = []
    for i in reversed(range(len(nums[0]))):
        new_num = ""
        for num in nums:
            new_num += num[i]
        new_nums.append(new_num)

    return new_nums


def get_input():
    input_path = "./" + sys.argv[1]
    file = open(input_path)
    result = [line for line in file]
    ops = result[-1].split()

    columns = []
    i_ops = []
    for i in range(len(result[-1])):
        if result[-1][i] != " ":
            i_ops.append(i)
    i_ops.append(len(result[-1]) + 1)

    for i in range(len(i_ops) - 1):
        column = []
        left = i_ops[i]
        right = i_ops[i + 1] - 1
        for line in result[:-1]:
            l = line + " "
            column.append(line[left:right])
        columns.append(column)
    return columns, ops


columns, ops = get_input()
print("Part 1:", part_1(columns, ops))
print("Part 2:", part_2(columns, ops))
