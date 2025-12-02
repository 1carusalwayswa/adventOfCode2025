# 2   02:56:35   03:31:18
'''
Forget to set alarm and use brute force.
missed a lot. :<
'''

import functools

from aocd.models import Puzzle
from util import ints

puzzle = Puzzle(2025, int("2"))

data = puzzle.input_data
# How to test with example data
test_data = puzzle.examples[0].input_data


# data = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"
# print(test_data)
# separate lines from data using ','
lines = data.replace('\n', '').split(',')

print(lines)
a_ans = 0
b_ans = 0
max_len = 0

def check_same_by_len(str_num:str, length:int) -> bool:
    if length == 0:
        return False
    idx = length
    if len(str_num) % length != 0:
        return False
    for i in range(length, len(str_num)):
        if str_num[i] != str_num[i % length]:
            return False
    return True

for line in lines:
    str_l, str_r = line.split('-')

    l_num = int(str_l)
    r_num = int(str_r)

    for num in range(l_num, r_num + 1):
        str_num = str(num)

        if check_same_by_len(str_num, ((len(str_num)) // 2)):
            if len(str_num) % 2 != 1:  
                # print(num, ((len(str_num)) // 2))
                a_ans += num

        for i in range(1, ((len(str_num)) // 2) + 1):
            # print(str_num, i)
            if check_same_by_len(str_num, i):
                b_ans += num
                break
        
# print(a_ans)
# print(b_ans)
puzzle.answer_a = a_ans
puzzle.answer_b = b_ans