# 10   00:38:53   11:57:32
'''
Typically learning new library moments.
Feels like twice this every year? :<
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

puzzle = Puzzle(2025, int("10"))

data = puzzle.input_data
test_data = puzzle.examples[0].input_data

lights = [] 
buttons = []
security_req = []

lines = data.split('\n')

print(len(lines))
for line in lines:
    bracket_match = re.search(r'\[(.*?)\]', line)
    if bracket_match:
        lights.append(bracket_match.group(1))
    
    parenthesis_matches = re.findall(r'\(([0-9,]+)\)', line)
    row_groups = []
    for match in parenthesis_matches:
        if ',' in match:
            row_groups.append([int(x) for x in match.split(',')])
        else:
            row_groups.append([int(match)])
    buttons.append(row_groups)
    
    brace_match = re.search(r'\{([0-9,]+)\}', line)
    if brace_match:
        security_req.append([int(x) for x in brace_match.group(1).split(',')])

a_ans = 0
b_ans = 0

@cache
def dfs(idx:int, cur:int, target:int, step:int) -> int:
    global buttons
    cur_button = buttons[idx]
    if cur == target:
        return 0
    
    if step >= 400:
        return float('inf')
    
    res = float('inf')
    for i in range(len(cur_button)):
        tmp_cur = cur
        for j in range(len(cur_button[i])):
            k = cur_button[i][j]
            # print(f'Line {idx}, ori_tmp_cur: {bin(tmp_cur)}, toggling button {k}')
            tmp_cur = tmp_cur ^ (1 << k)
            # print(f'tmp_cur after toggling button {bin(1<<k)}: {bin(tmp_cur)}')
        # print(f'Line {idx}, ori_cur:{bin(cur)}, tmp_cur: {bin(tmp_cur)}')
        tmp_res = dfs(idx, tmp_cur, target, step + 1)
        res = min(res, tmp_res + 1)
    
    return res

def solve_with_ortools(button_groups, sec_req):
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return None
    
    num_groups = len(button_groups)
    num_buttons = len(sec_req)
    
    x = []
    for i in range(num_groups):
        x.append(solver.IntVar(0, solver.infinity(), f'x_{i}'))
    
    for button_id in range(num_buttons):
        constraint_expr = 0
        for group_id in range(num_groups):
            if button_id in button_groups[group_id]:
                constraint_expr += x[group_id]
        solver.Add(constraint_expr == sec_req[button_id])
    
    objective = solver.Objective()
    for i in range(num_groups):
        objective.SetCoefficient(x[i], 1)
    objective.SetMinimization()
    
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        total_presses = sum(int(x[i].solution_value()) for i in range(num_groups))
        combination_counts = [int(x[i].solution_value()) for i in range(num_groups)]
        return total_presses, combination_counts
    else:
        return None
        
for i in range(len(lines)):
    light = lights[i]
    button_groups = buttons[i]
    sec_req = security_req[i]
    
    print(f"\n=== Line {i} ===")
    print(f"sec_req: {sec_req}")
    print(f"button_groups: {button_groups}")

    result = solve_with_ortools(button_groups, sec_req)
    if result:
        total_presses, combination_counts = result
        print(f"Solution found!")
        print(f"Total presses: {total_presses}")
        print(f"Combination usage: {combination_counts}")
        
        button_press_count = [0] * len(sec_req)
        for group_id, count in enumerate(combination_counts):
            for button_id in button_groups[group_id]:
                button_press_count[button_id] += count
        print(f"Verification - Button press counts: {button_press_count}")
        print(f"Expected: {sec_req}")
        
        b_ans += total_presses
    else:
        print(f"No solution found for line {i}")

    target_state = 0
    for j in range(len(light)):
        if light[j] == '#':
            target_state |= (1 << j)

    

print(a_ans)
print(b_ans)
# puzzle.answer_a = a_ans
# puzzle.answer_b = b_ans