# Find the two entries that sum to 2020; what do you get if you multiply them together?

goal = 2020

def read_input(file_loc):
    with open(file_loc, "r") as f:
        values = f.read().split()
    values = [int(i) for i in values]
    return values

# for part 1
def get_2_nums(values, goal):
    copy_values = values.copy()
    for val in values:
        copy_values.remove(val)
        if (goal - val) in copy_values:
            return [val, goal-val]
    return None

# for part 2
def get_3_nums(values):
    copy_values = values.copy()
    for val in values:
        copy_values.remove(val)
        sub_goal = goal - val
        res = get_2_nums(copy_values, sub_goal)
        if res is not None:
            return [val, res[0], res[1]]

values = read_input("../Inputs/day1.txt")
res = get_2_nums(values, goal)
num1 = res[0]
num2 = res[1]
print('Part 1:')
print(f'Num 1: {num1} Num 2: {num2} Product: {num1 * num2}')

res = get_3_nums(values)
num1 = res[0]
num2 = res[1]
num3 = res[2]
print('Part 2:')
print(f'Num 1: {num1} Num 2: {num2} Num 3: {num3} Product: {num1 * num2 * num3}')
