import sys
sys.setrecursionlimit(5000)

def read_input(file_loc):
    with open(file_loc, "r") as f:
        return [list(x) for x in f.read().split("\n")]

trail_map = read_input("../Inputs/test.txt")
all_paths = []

def getNextStep(row, col, stepped_tiles):
    if row >= len(trail_map) or col >= len(trail_map[0]) or row < 0 or col < 0:
        return "out_of_bounds"
    if trail_map[row][col] == "#":
        return "forest"
    if (row, col) in stepped_tiles:
        return "stepped"
    return trail_map[row][col]

def takeStep(row, col, stepped_tiles):
    stepped_tiles.append((row, col))
    # print(stepped_tiles)
    if row == (len(trail_map)-1) and col == len(trail_map[0])-2:
        # DONE
        # print("DONEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        all_paths.append(stepped_tiles.copy())
    else:
        # get path option for NORTH
        nextStep = getNextStep(row-1, col, stepped_tiles)
        # print(f'Next NORTH step: {nextStep}')
        if nextStep == ".":
            north_stepped_tiles = stepped_tiles.copy()
            takeStep(row-1, col, north_stepped_tiles)
        elif nextStep == "<":
            north_stepped_tiles = stepped_tiles.copy()
            north_stepped_tiles.append((row-1, col))
            takeStep(row-1, col-1, north_stepped_tiles)
        elif nextStep == ">":
            north_stepped_tiles = stepped_tiles.copy()
            north_stepped_tiles.append((row-1, col))
            takeStep(row-1, col+1, north_stepped_tiles)
        # get path option for EAST
        nextStep = getNextStep(row, col+1, stepped_tiles)
        # print(f'Next EAST step: {nextStep}')
        if nextStep == ".":
            east_stepped_tiles = stepped_tiles.copy()
            takeStep(row, col+1, east_stepped_tiles)
        elif nextStep == "v":
            east_stepped_tiles = stepped_tiles.copy()
            east_stepped_tiles.append((row, col+1))
            takeStep(row+1, col+1, east_stepped_tiles)
        elif nextStep == ">":
            east_stepped_tiles = stepped_tiles.copy()
            east_stepped_tiles.append((row, col+1))
            takeStep(row, col+2, east_stepped_tiles)
        # get path option for SOUTH
        nextStep = getNextStep(row+1, col, stepped_tiles)
        # print(f'Next SOUTH step: {nextStep}')
        if nextStep == ".":
            south_stepped_tiles = stepped_tiles.copy()
            takeStep(row+1, col, south_stepped_tiles)
        elif nextStep == "v":
            south_stepped_tiles = stepped_tiles.copy()
            south_stepped_tiles.append((row+1, col))
            takeStep(row+2, col, south_stepped_tiles)
        elif nextStep == ">":
            south_stepped_tiles = stepped_tiles.copy()
            south_stepped_tiles.append((row+1, col))
            takeStep(row+1, col+1, south_stepped_tiles)
        elif nextStep == "<":
            south_stepped_tiles = stepped_tiles.copy()
            south_stepped_tiles.append((row+1, col))
            takeStep(row+1, col-1, south_stepped_tiles)
        # get path option for WEST
        nextStep = getNextStep(row, col-1, stepped_tiles)
        # print(f'Next WEST step: {nextStep}')
        if nextStep == ".":
            west_stepped_tiles = stepped_tiles.copy()
            takeStep(row, col-1, west_stepped_tiles)
        elif nextStep == "v":
            west_stepped_tiles = stepped_tiles.copy()
            west_stepped_tiles.append((row, col-1))
            takeStep(row+1, col-1, west_stepped_tiles)
        elif nextStep == "<":
            west_stepped_tiles = stepped_tiles.copy()
            west_stepped_tiles.append((row, col-1))
            takeStep(row, col-2, west_stepped_tiles)

takeStep(0, 1, [])

max_path_len = 0
for path in all_paths:
    if len(path) > max_path_len:
        max_path_len = len(path)
        # print((path))
print(f'Max path length: {max_path_len-1}')

