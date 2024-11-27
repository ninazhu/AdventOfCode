def read_input(file_loc):
    with open(file_loc, "r") as f:
        return f.read().split("\n")

heightmap = read_input("../Inputs/day9.txt")

height = len(heightmap)
width = len(heightmap[0])
flatmap = [int(x) for x in ''.join(heightmap)]

def get_upper(ind):
    if ind < width:
        return 9, None
    return flatmap[ind-width], ind-width

def get_lower(ind):
    if ind > len(flatmap) - width - 1:
        return 9, None
    return flatmap[ind+width], ind+width

def get_left(ind):
    if ind % width == 0:
        return 9, None
    return flatmap[ind - 1], ind - 1

def get_right(ind):
    if (ind + 1) % width == 0:
        return 9, None
    return flatmap[ind + 1], ind + 1

def get_basin_points(ind, basin_points):
    basin_points.add(ind)
    upper, ind_upper = get_upper(ind)
    lower, ind_lower = get_lower(ind)
    left, ind_left = get_left(ind)
    right, ind_right = get_right(ind)
    if ind_upper is not None and upper != 9:
        if ind_upper not in basin_points:
            basin_points.union(get_basin_points(ind_upper, basin_points))
    if ind_lower is not None and lower != 9:
        if ind_lower not in basin_points:
            basin_points.union(get_basin_points(ind_lower, basin_points))
    if ind_left is not None and left != 9:
        if ind_left not in basin_points:
            basin_points.union(get_basin_points(ind_left, basin_points))
    if ind_right is not None and right != 9:
        if ind_right not in basin_points:
            basin_points.union(get_basin_points(ind_right, basin_points))
    return basin_points

sum_risk_levels = 0
len_basins = []
for ind, point in enumerate(flatmap):
    if point == 9:
        continue
    upper, ind_upper = get_upper(ind)
    lower, ind_lower = get_lower(ind)
    left, ind_left = get_left(ind)
    right, ind_right = get_right(ind)
    if point < upper and point < lower and point < left and point < right:
        sum_risk_levels = sum_risk_levels + point + 1
        # Part 2
        basin_points = get_basin_points(ind, set())
        len_basins.append(len(basin_points))

len_basins.sort()
result = 1
for i in len_basins[len(len_basins)-3:]:
    result = result * i

print(f'Part 1: {sum_risk_levels}')
print(f'Part 2: {result}')
