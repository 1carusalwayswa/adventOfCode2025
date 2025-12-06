# 6   00:13:50   01:10:48
'''
Typically simulate the process described in the problem statement, typically complicated implementation.
will learn better ways later.
'''

import copy
import functools

from aocd.models import Puzzle
from util import ints
import time

puzzle = Puzzle(2025, int("6"))

data = puzzle.input_data
test_data = puzzle.examples[0].input_data

lines = data.split('\n')

num_list = []
op_list = []

for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    if i == len(lines) - 1:
        op_list = line.split()
    else:
        num_list.append(list(map(int, line.split())))

last_line = num_list[0]
for i in range(1, len(num_list)):
    num_line = num_list[i]
    for j in range(len(op_list)):
        if op_list[j] == '+':
            last_line[j] += num_line[j]
        elif op_list[j] == '*':
            last_line[j] *= num_line[j]

a_ans = 0
for num in last_line:
    a_ans += num

grid = []
for i, line in enumerate(lines):
    if i == len(lines) - 1:
        continue
    grid.append(list(line))

def find_num_str_(start: int):
    res = []
    for i, line in enumerate(grid):
        # print("now line:", line)
        cur_str = ''
        digit_found = False
        for j, ch in enumerate(line):
            if j < start:
                continue
            if ch >= '0' and ch <= '9':
                digit_found = True
            if ch == ' ' and digit_found:
                break
            cur_str += ch
        res.append(cur_str)
    return res
            

b_ans = 0
op_str = lines[-1]
for i, ch in enumerate(op_str):
    if ch == '+' or ch == '*':
        num_strs = find_num_str_(i)
        # fine max len in num_strs
        max_len = 0
        for s in num_strs:
            if len(s) > max_len:
                max_len = len(s)
        for i in range(len(num_strs)):
            while len(num_strs[i]) < max_len:
                num_strs[i] += ' '
            # print(num_strs[i])
        
        tmp_op_sum = 1 if ch == '*' else 0
        for i in range(max_len - 1, -1, -1):
            col_sum = 0
            for s in num_strs:
                if i < len(s) and s[i] >= '0' and s[i] <= '9':
                    col_sum = col_sum * 10 + int(s[i])
            # print("col sum for + at", i, "is", col_sum)
            if ch == '+':
                tmp_op_sum += col_sum
            elif ch == '*':
                tmp_op_sum *= col_sum
            # print("tmp_op_sum now:", tmp_op_sum)
        b_ans += tmp_op_sum


print(a_ans)
print(b_ans)
# puzzle.answer_b = b_ans# puzzle.answer_a = a_ansprint(b_ans)print(a_ans)print(a_ans)
# print(b_ans)
puzzle.answer_a = a_ans
puzzle.answer_b = b_ans