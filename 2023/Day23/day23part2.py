import sys
sys.setrecursionlimit(10**6)

import pickle as cPickle

class MemoizeMutable:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args, **kwds):
        # import cPickle
        str = cPickle.dumps(args, 1)+cPickle.dumps(kwds, 1)
        if str not in self.memo: 
            # print "miss"  # DEBUG INFO
            self.memo[str] = self.fn(*args, **kwds)
        # else:
            # print "hit"  # DEBUG INFO

        return self.memo[str]

def read_input(file_loc):
    with open(file_loc, "r") as f:
        return [list(x) for x in f.read().split("\n")]

def getNextStep(row, col):
    if row >= len(trail_map) or col >= len(trail_map[0]) or row < 0 or col < 0:
        return "out_of_bounds"
    if trail_map[row][col] == "#":
        return "forest"
    return trail_map[row][col]

trail_map = read_input("../Inputs/test.txt")

# build graph of paths
path_dict = {}
for x, row in enumerate(trail_map):
    for y, _ in enumerate(row):
        if trail_map[x][y] != ("#"):
            # get North
            if getNextStep(x-1, y) not in ("forest", "out_of_bounds"):
                if f'{x},{y}' not in path_dict:
                    path_dict[f'{x},{y}'] = [f'{x-1},{y}']
                else:
                    path_dict[f'{x},{y}'].append(f'{x-1},{y}')
            # get East
            if getNextStep(x, y+1) not in ("forest", "out_of_bounds"):
                if f'{x},{y}' not in path_dict:
                    path_dict[f'{x},{y}'] = [f'{x},{y+1}']
                else:
                    path_dict[f'{x},{y}'].append(f'{x},{y+1}')
            # get West
            if getNextStep(x, y-1) not in ("forest", "out_of_bounds"):
                if f'{x},{y}' not in path_dict:
                    path_dict[f'{x},{y}'] = [f'{x},{y-1}']
                else:
                    path_dict[f'{x},{y}'].append(f'{x},{y-1}')
            # get South
            if getNextStep(x+1, y) not in ("forest", "out_of_bounds"):
                if f'{x},{y}' not in path_dict:
                    path_dict[f'{x},{y}'] = [f'{x+1},{y}']
                else:
                    path_dict[f'{x},{y}'].append(f'{x+1},{y}')
# print(path_dict)

# traverse paths
path_lengths = []
final_tile = f'{len(trail_map)-1},{len(trail_map[0])-2}'

@MemoizeMutable
def traverse(trail_path):
    last_tile = trail_path[-1]
    if last_tile == final_tile:
        path_lengths.append(len(trail_path)-1)
        # print(len(trail_path)-1)
    for nextStep in path_dict[last_tile]:
        # print(f'Current Tile: {last_tile}, Next Step: {nextStep}')
        if nextStep not in trail_path:
            # print(f'Current Tile: {last_tile}, Next Step: {nextStep}')
            traverse(trail_path + [nextStep])

traverse(["0,1"])

print(f'Max path length: {max(path_lengths)}')

