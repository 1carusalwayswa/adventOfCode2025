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
# create a vis array for grid
vis = [[False] * len(grid[0]) for _ in range(len(grid))]

a_ans = 0
b_ans = 0

@cache
def dfs(i:int, j:int) -> int:
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return 1
    
    if vis[i][j]:
        return 0
    
    if grid[i][j] != '^':
        vis[i][j] = True
        res = dfs(i + 1, j)
        vis[i][j] = False
        return res
    
    global a_ans
    a_ans += 1
    
    vis[i][j] = True
    res_l = dfs(i + 1, j - 1)
    res_r = dfs(i + 1, j + 1)
    vis[i][j] = False
    return res_l + res_r

for i in range(len(grid)):
    flag = False
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            b_ans = dfs(i, j)
            flag = True
            break
    if flag:
        break

print(a_ans)
print(b_ans)
puzzle.answer_a = a_ans
puzzle.answer_b = b_ans