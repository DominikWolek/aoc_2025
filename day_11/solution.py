#!/usr/bin/env python
import sys


def solve(to_check, input):
    result = 0
    for path in to_check:
        paths_cnt = 1

        for i in range(len(path) - 1):
            start = path[i]
            end = path[i + 1]
            paths = {(end, end): 1}
            for x in path:
                if x != start and x != end:
                    paths[(x, end)] = 0
            fill_paths(start, end, input, paths)
            paths_cnt *= paths[(start, end)]
        result += paths_cnt

    return result


def fill_paths(start, end, conns, paths):
    end_paths = 0
    for out in conns.get(start, []):
        if (out, end) not in paths:
            paths = fill_paths(out, end, conns, paths)
        end_paths += paths[(out, end)]

    paths[(start, end)] = end_paths
    return paths


def get_input():
    input_path = "./" + sys.argv[1]
    file = open(input_path)
    result = [line.split() for line in file]
    result = [(line[0][:-1], line[1:]) for line in result]

    conns = {}
    for line in result:
        (start, outs) = line
        conns[start] = outs

    return conns


input = get_input()
a = 'svr'
b = 'fft'
c = 'dac'
o = 'out'
y = 'you'

print("Part 1:", solve([[y, o]], input))
print("Part 2:", solve([[a, b, c, o], [a, c, b, o]], input))
