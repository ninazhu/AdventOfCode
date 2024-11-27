
def read_input(file_loc):
    with open(file_loc, "r") as f:
        return f.read().split("\n")

cave_connections = read_input("../Inputs/day12.txt")

cave_map = {}
for conn in cave_connections:
    conn_split = conn.split('-')
    node1 = conn_split[0]
    node2 = conn_split[1]
    if not cave_map.get(node1):
        cave_map[node1] = [node2]
    else:
        cave_map[node1].append(node2)
    if node1 != 'start':
        if not cave_map.get(node2):
            cave_map[node2] = [node1]
        else:
            cave_map[node2].append(node1)

path_list = []
def traverse(curr_cave, curr_path):
    if curr_cave == 'end':
        path_list.append(curr_path)
        return
    options = cave_map[curr_cave]
    for opt in options:
        if opt.islower() and opt in curr_path:
            continue
        else:
            new_path = curr_path.copy()
            new_path.append(opt)
            traverse(opt, new_path)

traverse('start', ['start'])
print(f'Part 1: {len(path_list)}')


def path_has_double_small_cave(curr_path):
    lowercases = []
    for i in curr_path:
        if i.islower() and i in lowercases:
            return True
        lowercases.append(i)
    return False

path_list = []
def traverse(curr_cave, curr_path):
    if curr_cave == 'end':
        path_list.append(curr_path)
        return
    options = cave_map[curr_cave]
    for opt in options:
        if opt.islower() and opt in curr_path and path_has_double_small_cave(curr_path):
            continue
        else:
            new_path = curr_path.copy()
            new_path.append(opt)
            traverse(opt, new_path)

traverse('start', ['start'])
print(f'Part 2: {len(path_list)}')