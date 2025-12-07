#  7   00:13:38   00:21:34
'''
typical cache moment.
'''

import copy
import functools
from functools import cache

from aocd.models import Puzzle
from util import ints
import time

puzzle = Puzzle(2025, int("7"))

data = puzzle.input_data
test_data = puzzle.examples[0].input_data

# learned from others
lines = data.split('\n')
grid = [list(line) for line in lines]

a_ans = 0
b_ans = 0

def dfs_a(i:int, j:int) -> None:
    global a_ans
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return
    
    if grid[i][j] == '|':
        return
    
    if grid[i][j] != '^':
        grid[i][j] = '|'
        dfs_a(i + 1, j)
        return
    
    if grid[i][j] == '^':
        a_ans += 1
        dfs_a(i + 1, j - 1)
        dfs_a(i + 1, j + 1)

for i in range(len(grid)):
    flag = False
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            dfs_a(i, j)
            flag = True
            break
    if flag:
        break

# reset grid
grid = [list(line) for line in lines]

@cache
def dfs_b(i:int, j:int) -> None:
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return 1
    
    if grid[i][j] != '^':
        return dfs_b(i + 1, j)
    
    return dfs_b(i + 1, j - 1) + dfs_b(i + 1, j + 1)

for i in range(len(grid)):
    flag = False
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            b_ans = dfs_b(i, j)
            flag = True
            break
    if flag:
        break

print(a_ans)
print(b_ans)
puzzle.answer_a = a_ans
puzzle.answer_b = b_ans