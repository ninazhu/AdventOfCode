def read_input(file_loc):
    with open(file_loc, "r") as f:
        return [x.split(' -> ') for x in f.read().split("\n")]

lines = read_input("../Inputs/day5.txt")

grid = {}

def mark_grid(key):
    if grid.get(key) is not None:
            grid[key] = grid[key] + 1
    else:
        grid[key] = 1

def mark_grid_horizontal(x, y1, y2):
    for y in range(y1, y2 + 1):
        key = f'{x},{y}'
        mark_grid(key)

def mark_grid_vertical(y, x1, x2):
    for x in range(x1, x2 + 1):
        key = f'{x},{y}'
        mark_grid(key)

def mark_grid_diagonal(x1, y1, x2, y2):
    if x1 > x2:
        for i, x in enumerate(range(x2, x1 + 1)):
            if y2 > y1:
                key = f'{x},{y2 - i}'
            else:
                key = f'{x},{y2 + i}'
            mark_grid(key)
    else:
        for i, x in enumerate(range(x1, x2 + 1)):
            if y2 > y1:
                key = f'{x},{y1 + i}'
            else:
                key = f'{x},{y1 - i}'
            mark_grid(key)                

for line in lines:
    start = line[0].split(',')
    start_x = int(start[0])
    start_y = int(start[1])
    end = line[1].split(',')
    end_x = int(end[0])
    end_y = int(end[1])
    # check if horizontal or vertical line
    if start_x == end_x:
        if start_y >= end_y:
            mark_grid_horizontal(start_x, end_y, start_y)
        else:
            mark_grid_horizontal(start_x, start_y, end_y)
    elif start_y == end_y:
        if start_x >= end_x:
            mark_grid_vertical(start_y, end_x, start_x)
        else:
            mark_grid_vertical(start_y, start_x, end_x)
    else:   # diagonal
        print(f'{start_x},{start_y} -> {end_x},{end_y}')
        mark_grid_diagonal(start_x, start_y, end_x, end_y)  # for part 2
        # continue

print(f'Result: {len([v for v in grid.values() if int(v) >= 2])}')
