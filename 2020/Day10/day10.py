# What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?

def read_input(file_loc):
    with open(file_loc, "r") as f:
        return sorted(int(i) for i in f)

def tribonacci(num):
    if num in [0, 1]:
        return 1
    elif num == 2:
        return 2
    return tribonacci(num-1) + tribonacci(num-2) + tribonacci(num-3)

adapters = read_input("../Inputs/day10.txt")

curr_jolt = 0
count = 1
multiplier = 0
diff_list = []

for adapter in adapters:
    diff = adapter - curr_jolt
    diff_list.append(diff)
    curr_jolt = adapter
    if diff == 1:
        multiplier = multiplier + 1
    else:
        count = count * tribonacci(multiplier)
        multiplier = 0

num_1 = diff_list.count(1)
num_3 = diff_list.count(3) + 1
print(f'Part 1:\n1-jolt x 3-jolt is {num_1 * num_3}')
print(f'Part 2:\nPossible combos: {count}')
