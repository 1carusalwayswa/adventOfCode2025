# 1   00:16:18   00:26:43
'''
Warmup for AOC 2025.
'''

import functools

from aocd.models import Puzzle
from util import ints

puzzle = Puzzle(2025, int("1"))

data = puzzle.input_data

# data = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"

lines = data.splitlines()

cur_num = 50
ans = 0
b_ans = 0
for line in lines:
    op = 1
    if line[0] == "L":
        op = -1
    num = int(line[1:])
    new_num = (cur_num + (op * num) + 100) % 100
    cnt = num // 100
    b_ans += cnt

    if op == -1 and new_num > cur_num and cur_num != 0:
        b_ans += 1
    elif op == 1 and new_num < cur_num and cur_num != 0:
        b_ans += 1
    elif new_num == 0:
        b_ans += 1
    cur_num = new_num

    if cur_num == 0:
        ans += 1

print(ans)
print(b_ans)
    

puzzle.answer_a = ans
puzzle.answer_b = b_ans