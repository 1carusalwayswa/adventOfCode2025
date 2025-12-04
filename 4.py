# 4   00:12:12   00:19:28
'''
best time so far, pretty easy problem.
'''

import copy
import functools

from aocd.models import Puzzle
from util import ints

puzzle = Puzzle(2025, int("4"))

data = puzzle.input_data
# How to test with example data
test_data = puzzle.examples[0].input_data

lines = data.split('\n')
grid = [list(line) for line in lines]

def check_neghbors(i:int, j:int) -> None:
    cnt = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dir in directions:
        ni, nj = i + dir[0], j + dir[1]
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
            if grid[ni][nj] == '@':
                cnt += 1
    return cnt < 4

a_ans = 0
b_ans = 0
first_update = True

while True:
    changed = False
    new_grid = copy.deepcopy(grid) 
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                if check_neghbors(i, j):
                    b_ans += 1
                    if first_update:
                        a_ans += 1
                    new_grid[i][j] = 'x'
                    changed = True
    grid = new_grid
    first_update = False
    if not changed:
        break

# for i in range(len(grid)):
#     print(''.join(grid[i]))

# print("----")
# for i in range(len(tmp_grid)):
#     print(''.join(tmp_grid[i]))

# print(a_ans)
# print(b_ans)
puzzle.answer_a = a_ans
puzzle.answer_b = b_ans