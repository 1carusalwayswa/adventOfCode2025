# 4   00:05:32   00:16:57
'''
best time so far, pretty easy problem.
learned interval merge from others, my way is too inefficient.
'''

import copy
import functools

from aocd.models import Puzzle
from util import ints
import time

puzzle = Puzzle(2025, int("5"))

data = puzzle.input_data
test_data = puzzle.examples[0].input_data

# learned from others
lines = [list(map(int, l.strip().split('-'))) for l in data.split('\n') if l.strip()]
range_list = [l for l in lines if len(l) == 2]
num_list = [l[0] for l in lines if len(l) == 1]

a_ans = 0
b_ans = 0

for num in num_list:
    for l, r in range_list:
        if l <= num <= r:
            a_ans += 1
            break

# original way to parse input
# for line in lines:
#     if line.find('-') != -1:
#         l, r = line.split('-')
#         range_list.append((int(l), int(r)))
#     else:
#         if line == '':
#             continue
#         num = int(line)
#         for r in range_list:
#             if r[0] <= num <= r[1]:
#                 a_ans += 1
#                 break

# My very inefficient way to merge intervals, but works
# t1 = time.perf_counter()
# updatad = True
# while updatad:
#     updatad = False
#     for i in range(len(range_list)):
#         for j in range(i + 1, len(range_list)):
#             l1, r1 = range_list[i]
#             l2, r2 = range_list[j]
#             if not (r1 < l2 or r2 < l1):
#                 nl = min(l1, l2)
#                 nr = max(r1, r2)
#                 range_list.pop(j)
#                 range_list.pop(i)
#                 range_list.append( (nl, nr) )
#                 updatad = True
#                 break
#         if updatad:
#             break
# for l,r in range_list:
#     b_ans += (r - l + 1)
# t2 = time.perf_counter()
# print("My merge time:", t2 - t1)
# my_merge_time = t2 - t1
#     # print(l, r)

# other people's efficient way to merge intervals by sorting
# faster 1000x than mine
# t1 = time.perf_counter()
last_r = -1
for l, r in sorted(range_list):
    if r <= last_r:
        continue
    l = max(l, last_r + 1)
    b_ans += (r - l + 1)
    last_r = r
# t2 = time.perf_counter()

print(a_ans)
print(b_ans)
# puzzle.answer_a = a_ans
# puzzle.answer_b = b_ans