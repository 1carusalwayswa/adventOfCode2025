# 11   00:09:45   00:40:05
'''
DAG problem.
'''

import copy
from functools import cache
from math import sqrt
from shapely.geometry import Point, Polygon, box
import re
from ortools.linear_solver import pywraplp

from aocd.models import Puzzle
from util import ints
import time

puzzle = Puzzle(2025, int("11"))

data = puzzle.input_data
test_data = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

lines = data.split('\n')

a_ans = 0
b_ans = 0

adjacency_list = {}

max_len = 0
for line in lines:
    if ':' in line:
        parts = line.split(':')
        node = parts[0].strip()
        neighbors = parts[1].strip().split()
        
        adjacency_list[node] = neighbors
        if len(neighbors) > max_len:
            max_len = len(neighbors)

# input data has no cycles
memo = {}
def count_paths(start, end):
    if start == end:
        return 1
    
    if start in memo:
        return memo[start]
    
    total = 0
    for neighbor in adjacency_list.get(start, []):
        total += count_paths(neighbor, end)
    
    memo[start] = total
    return total

svc_fft = count_paths('svr', 'fft')
memo = {}
svc_dac = count_paths('svr', 'dac')
memo = {}
fft_dac = count_paths('fft', 'dac')
memo = {}
dac_fft = count_paths('dac', 'fft')
memo = {}
fft_out = count_paths('fft', 'out')
memo = {}
dac_out = count_paths('dac', 'out')

part_1 = svc_fft * fft_dac * dac_out
part_2 = svc_dac * dac_fft * fft_out

a_ans = count_paths('you', 'out')
b_ans = part_1 + part_2

print(a_ans)
print(b_ans)
puzzle.answer_a = a_ans
puzzle.answer_b = b_ans