# How many trees would you encounter?

def read_input(file_loc):
    with open(file_loc, "r") as f:
        values = f.read().split('\n')
    values = [i for i in values]
    return values

def get_next_pos(curr_row, curr_col, steps_right, steps_down):
    next_col = curr_col + steps_right
    if next_col > map_width - 1:
        next_col = next_col - map_width
    return curr_row + steps_down, next_col

def traverse(steps_right, steps_down):
    count = 0
    curr_row = 0
    curr_col = 0
    while curr_row < map_length:
        if tree_map[curr_row][curr_col] == '#':
            count = count + 1
        curr_row, curr_col = get_next_pos(curr_row, curr_col, steps_right, steps_down)
    return count

tree_map = read_input("../Inputs/day3.txt")
map_length = len(tree_map)
map_width = len(tree_map[0])

ans1 = traverse(1, 1)
ans2 = traverse(3, 1)
ans3 = traverse(5, 1)
ans4 = traverse(7, 1)
ans5 = traverse(1, 2)

print(f'Part 1:\nNumber of trees for 3 right 1 down: {ans2}')
print(f'Part 2:\nProduct of 5 answers: {ans1 * ans2 * ans3 * ans4 * ans5}')
