import sys

sys.setrecursionlimit(5000)

def read_input(file_loc):
    with open(file_loc, "r") as f:
        return [list(x) for x in f.read().split("\n")]

trail_map = read_input("../Inputs/test.txt")

for x, row in enumerate(trail_map):
    for y, _ in enumerate(row):
        if trail_map[x][y] not in (".","#"):
            trail_map[x][y] = "."

path_lengths = []
path_dict = {}

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
        path_lengths.append(len(stepped_tiles))
    else:
        # get path option for NORTH
        nextStep = getNextStep(row-1, col, stepped_tiles)
        # print(f'Next NORTH step: {nextStep}')
        if nextStep == ".":
            north_stepped_tiles = stepped_tiles.copy()
            takeStep(row-1, col, north_stepped_tiles)
        # get path option for EAST
        nextStep = getNextStep(row, col+1, stepped_tiles)
        # print(f'Next EAST step: {nextStep}')
        if nextStep == ".":
            east_stepped_tiles = stepped_tiles.copy()
            takeStep(row, col+1, east_stepped_tiles)
        # get path option for SOUTH
        nextStep = getNextStep(row+1, col, stepped_tiles)
        # print(f'Next SOUTH step: {nextStep}')
        if nextStep == ".":
            south_stepped_tiles = stepped_tiles.copy()
            takeStep(row+1, col, south_stepped_tiles)
        # get path option for WEST
        nextStep = getNextStep(row, col-1, stepped_tiles)
        # print(f'Next WEST step: {nextStep}')
        if nextStep == ".":
            west_stepped_tiles = stepped_tiles.copy()
            takeStep(row, col-1, west_stepped_tiles)

takeStep(0, 1, [])

print(f'Max path length: {max(path_lengths)-1}')

