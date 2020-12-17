# How many cubes are left in the active state after the sixth cycle?

def read_input(file_loc):
    with open(file_loc, "r") as f:
        values = f.read().split('\n')
    values = [list(i) for i in values]
    return values

def get_neighbor_coords(coord):
    neigh_coords = []
    x = coord[0]
    y = coord[1]
    z = coord[2]
    w = coord[3]
    for x_new in range(x-1, x+2):
        for y_new in range(y-1, y+2):
            for z_new in range(z-1, z+2):
                for w_new in range(w-1, w+2):
                    neigh_coords.append((x_new, y_new, z_new, w_new))
    neigh_coords.remove(coord)
    return neigh_coords

init_cubes = read_input("../Inputs/day17.txt")
min_x = -1
min_y = -1
min_z = -1
min_w = -1
max_x = len(init_cubes[0])
max_y = len(init_cubes)
max_z = 1
max_w = 1

active_coords = []
for x, row in enumerate(init_cubes):
    for y, cube in enumerate(row):
        if cube == '#':
            active_coords.append((x, y, 0, 0))

def run_cycle(min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w, active_coords):
    new_active_coords = []
    for x_new in range(min_x, max_x + 1):
        for y_new in range(min_y, max_y + 1):
            for z_new in range(min_z, max_z + 1):
                for w_new in range(min_w, max_w + 1):
                    curr_coord = (x_new, y_new, z_new, w_new)
                    is_active = curr_coord in active_coords
                    neigh_coords = get_neighbor_coords(curr_coord)
                    count = len(set(neigh_coords) & set(active_coords))
                    if is_active:
                        if count in [2, 3]:
                            new_active_coords.append(curr_coord)
                    else:
                        if count == 3:
                            new_active_coords.append(curr_coord)
    return new_active_coords

curr_active_coords = active_coords
for i in range(6):
    new_active_coords = run_cycle(min_x, max_x, min_y, max_y, min_z, max_z, min_w, max_w, curr_active_coords)          
    curr_active_coords = new_active_coords
    min_x = min_x - 1
    min_y = min_y - 1
    min_z = min_z - 1
    max_x = max_x + 1
    max_y = max_y + 1
    max_z = max_z + 1
    min_w = min_w - 1
    max_w = max_w + 1

print(f'Part 2:\n Number of active cubes: {len(curr_active_coords)}')
