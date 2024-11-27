def read_input(file_loc):
    with open(file_loc, "r") as f:
        return [x.split(" ") for x in f.read().split('\n')]

directions = read_input("../Inputs/day2.txt")
horizontal = 0
depth = 0

for dir in directions:
    if dir[0] == 'forward':
        horizontal = horizontal + int(dir[1])
    elif dir[0] == 'up':
        depth = depth - int(dir[1])
    elif dir[0] == 'down':
        depth = depth + int(dir[1])
    else:
        print("ERROR: unexpected direction")

print(f'Part 1: {horizontal * depth}')

aim = 0
horizontal = 0
depth = 0

for dir in directions:
    if dir[0] == 'down':
        aim = aim + int(dir[1])
    elif dir[0] == 'up':
        aim = aim - int(dir[1])
    elif dir[0] == 'forward':
        horizontal = horizontal + int(dir[1])
        depth = depth + aim * int(dir[1])
    else:
        print("ERROR: unexpected direction")

print(f'Part 2: {horizontal * depth}')
