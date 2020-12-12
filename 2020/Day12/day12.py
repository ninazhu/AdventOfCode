# What is the Manhattan distance between that location and the ship's starting position?

compass = ['S', 'W', 'N', 'E']

def read_input(file_loc):
    with open(file_loc, "r") as f:
        return f.read().split("\n")

def move_cardinal_dir(x, y, instruction, distance):
    if instruction == 'N':
        y = y + distance
    elif instruction == 'S':
        y = y - distance
    elif instruction == 'E':
        x = x + distance
    else:
        x = x - distance
    return x, y

def move_ship(x, y, instruction, distance, facing_dir):
    if instruction == 'L':
        facing_dir = compass[compass.index(facing_dir) - int(distance / 90)]
    elif instruction == 'R':
        facing_dir = compass[int((compass.index(facing_dir) + (distance / 90)) % 4)]
    elif instruction == 'F':
        x, y = move_cardinal_dir(x, y, facing_dir, distance)
    else:
        x, y = move_cardinal_dir(x, y, instruction, distance)
    return x, y, facing_dir

directions = read_input("../Inputs/day12.txt")
x = 0
y = 0
facing_dir = 'E'
for direction in directions:
    instruction = direction[0]
    distance = int(direction[1:])
    x, y, facing_dir = move_ship(x, y, instruction, distance, facing_dir)

print(f"Part 1:\n Manhattan distance is {abs(x) + abs(y)}")

# part 2

def rotate_clockwise(x, y):
    return y, -x

def rotate_counterclockwise(x, y):
    return -y, x

def move_ship_2(x, y, w_x, w_y, instruction, distance):
    if instruction == 'L':
        for i in range(0, int(distance / 90)):
            w_x, w_y = rotate_counterclockwise(w_x, w_y)
            i = i + 1 
    elif instruction == 'R':
        for i in range(0, int(distance / 90)):
            w_x, w_y = rotate_clockwise(w_x, w_y)
            i = i + 1
    elif instruction == 'F':
        if w_x >= 0:
            facing_dir_x = 'E'
        else:
            facing_dir_x = 'W'
        if w_y >= 0:
            facing_dir_y = 'N'
        else:
            facing_dir_y = 'S'
        x, y = move_cardinal_dir(x, y, facing_dir_x, distance * abs(w_x))
        x, y = move_cardinal_dir(x, y, facing_dir_y, distance * abs(w_y))
    else:
        w_x, w_y = move_cardinal_dir(w_x, w_y, instruction, distance)

    return x, y, w_x, w_y

x = 0
y = 0
w_x = 10
w_y = 1

for direction in directions:
    instruction = direction[0]
    distance = int(direction[1:])
    x, y, w_x, w_y = move_ship_2(x, y, w_x, w_y, instruction, distance)

print(f"Part 2:\n Manhattan distance: {abs(x) + abs(y)}")
