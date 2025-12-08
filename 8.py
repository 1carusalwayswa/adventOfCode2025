#  8   01:11:12   01:38:31
'''
To understand the problem is harder to solve it.
'''

import copy
import functools
from math import sqrt

from aocd.models import Puzzle
from util import ints
import time

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def get_size(self, x):
        return self.size[self.find(x)]

puzzle = Puzzle(2025, int("8"))

data = puzzle.input_data
test_data = puzzle.examples[0].input_data

# learned from others
lines = data.split('\n')

boxes = [tuple(line.split(',')) for line in lines]

a_ans = 0
b_ans = 0

def cal_straight_line_distance(x1:int, y1:int, z1:int, x2:int, y2:int, z2:int) -> None:
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

UnionFind_obj = UnionFind(len(boxes))

def connect_top_n_shortest_distance(n:int) -> float:
    global UnionFind_obj
    global a_ans, b_ans
    dis = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            x1, y1, z1 = map(int, boxes[i])
            x2, y2, z2 = map(int, boxes[j])
            distance = cal_straight_line_distance(x1, y1, z1, x2, y2, z2)
            dis.append((distance, i, j))
    dis.sort()

    for i in range(n):
        _, box_i, box_j = dis[i]
        if UnionFind_obj.connected(box_i, box_j):
            # remove this distance
            continue
        UnionFind_obj.union(box_i, box_j)
    
    set_size = []
    for i in range(len(boxes)):
        if UnionFind_obj.find(i) == i:
            set_size.append(UnionFind_obj.get_size(i))
    set_size.sort()
    a_ans = set_size[-1] * set_size[-2] * set_size[-3]

    # for part 2
    for i in range(n + 1, len(dis)):
        _, box_i, box_j = dis[i]
        if UnionFind_obj.connected(box_i, box_j):
            # remove this distance
            continue
        UnionFind_obj.union(box_i, box_j)
        if UnionFind_obj.get_size(box_i) == len(boxes):
            b_ans = int(boxes[box_i][0]) * int(boxes[box_j][0]) 
    return 0
    
connect_top_n_shortest_distance(1000)

print(a_ans)
print(b_ans)
puzzle.answer_a = a_ans
puzzle.answer_b = b_ans