# 3   00:13:24   00:31:42
'''
someone has crazy finish time, will learn it later.
'''

import functools

from aocd.models import Puzzle
from util import ints

puzzle = Puzzle(2025, int("3"))

data = puzzle.input_data
# How to test with example data
test_data = puzzle.examples[0].input_data

lines = data.split('\n')

a_ans = 0
b_ans = 0

def get_max_in_line_by_len(line:str, length:int) -> int:
    line = list(map(int, line))
    if length == 0:
        return 0
    cur_len = 0
    res = 0
    idx = 0

    # print(line)
    while cur_len < length:
        max_num = 0
        for i in range(idx, len(line) - length + cur_len + 1):
            if line[i] > max_num:
                max_num = line[i]
                idx = i + 1
        # print(max_num, idx - 1, cur_len, len(line) - length + cur_len + 1)
        res = res * 10 + max_num
        cur_len += 1
    # print("----")
    # print(res)
    return res

for line in lines:
    a_ans += get_max_in_line_by_len(line, 2)
    b_ans += get_max_in_line_by_len(line, 12)
        
print(a_ans)
print(b_ans)
puzzle.answer_a = a_ans
puzzle.answer_b = b_ans