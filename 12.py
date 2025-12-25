# 12   01:31:50   01:32:03
'''
Not very hard problem, as the input data is esay to handle.
Just need to be careful with the area calculation.
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

puzzle = Puzzle(2025, int("12"))

data = puzzle.input_data
test_data = puzzle.examples[0].input_data 

lines = data.split('\n')
a_ans = 0
b_ans = 0

queries = []
for line in lines:
    if 'x' in line:
        parts = line.split(':')
        size_str = parts[0].strip()
        numbers_str = parts[1].strip()
        
        width, height = map(int, size_str.split('x'))
        
        numbers = list(map(int, numbers_str.split()))
        
        total_need_area = 0
        for i, num in enumerate(numbers):
            total_need_area += 9 * num
        if total_need_area <= width * height:
            a_ans += 1

print(a_ans)
print(b_ans)
puzzle.answer_a = a_ans
# puzzle.answer_b = b_ans