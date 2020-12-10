# What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?

def read_input(file_loc):
    with open(file_loc, "r") as f:
        values = f.read().split('\n')
    values = [int(i) for i in values]
    values.sort()
    return values

adapters = read_input("../Inputs/day10.txt")

my_map = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7, 5: 13}

curr_jolt = 0
count = 1
multiplier = 0
diff_list = []

for i in range(0, len(adapters)):
    diff = adapters[i] - curr_jolt
    diff_list.append(diff)
    curr_jolt = adapters[i]
    if diff == 1:
        multiplier = multiplier + 1
    else:
        count = count * my_map.get(multiplier)
        multiplier = 0

num_1 = diff_list.count(1)
num_3 = diff_list.count(3) + 1
print(f'Part 1:\n1-jolt x 3-jolt is {num_1 * num_3}')
print(f'Part 2:\nPossible combos: {count}')

# 1 2 3 4 5 6
# 1 2 3 4 6
# 1 2 3 5 6
# 1 2 3 6
# 1 2 4 5 6
# 1 2 4 6
# 1 2 5 6
# 1 3 4 5 6
# 1 3 4 6
# 1 3 5 6
# 1 3 6
# 1 4 5 6
# 1 4 6