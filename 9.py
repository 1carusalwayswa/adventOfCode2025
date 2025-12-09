#  9   00:04:38   02:35:25
'''
Typically learning new library moments.
Feels like once this every year? :<
'''

import copy
import functools
from math import sqrt
from shapely.geometry import Point, Polygon, box

from aocd.models import Puzzle
from util import ints
import time

puzzle = Puzzle(2025, int("9"))

data = puzzle.input_data
test_data = puzzle.examples[0].input_data

lines = data.split('\n')
tiles = [tuple(map(int, line.split(','))) for line in lines]
max_x = max(x for x, y in tiles)
min_x = min(x for x, y in tiles)
set_tiles = set(tiles)
polygon = Polygon(tiles)

max_area = 0
for i in range(len(tiles)):
    for j in range(len(tiles)):
        x1, y1 = tiles[i]
        x2, y2 = tiles[j]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if area > max_area:
            max_area = area
a_ans = max_area

def is_rectangle_fully_inside(x1, y1, x2, y2, polygon):
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    
    rectangle = box(x1, y1, x2, y2)
    
    return polygon.covers(rectangle)

max_area = 0
for i in range(len(tiles)):
    for j in range(i+1, len(tiles)):
        x1, y1 = tiles[i]
        x2, y2 = tiles[j]
        
        if is_rectangle_fully_inside(x1, y1, x2, y2, polygon):
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > max_area:
                max_area = area

b_ans = max_area

print(a_ans)
print(b_ans)
puzzle.answer_a = a_ans
puzzle.answer_b = b_ans