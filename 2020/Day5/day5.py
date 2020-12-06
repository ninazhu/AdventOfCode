# What is the highest seat ID on a boarding pass?

import pandas as pd

def read_input(file_loc):
    with open(file_loc, "r") as f:
        values = f.read().split('\n')
    values = [i for i in values]
    return values

def get_num(value, valid_nums):
    # print(value + " : " + str(valid_nums))
    if len(valid_nums) == 2:
        if value in ['F', 'L']:
            # print(f"*****{value} {valid_nums[0]}")
            return valid_nums[0]
        return valid_nums[1]
    if value[0] in ['F', 'L']:
        return get_num(value[1:], valid_nums[:(len(valid_nums)//2)])
    else:
        return get_num(value[1:], valid_nums[(len(valid_nums)//2):])
max_rows = 128
max_cols = 8
total_rows = list(range(0, max_rows))
total_cols = list(range(0, max_cols))

values = read_input("../Inputs/day5.txt")

seat_ids = []
seat_map = pd.DataFrame(0, index=range(max_rows), columns=range(max_cols))
for val in values:
    row = get_num(val[:7], total_rows)
    col = get_num(val[-3:], total_cols)
    seat_id = row * 8  + col
    seat_ids.append(seat_id)
    seat_map[col][row] = 1

def find_my_seat(seat_map):
    flat_map = list(seat_map.values.flatten())
    for i in range(1, len(flat_map) - 1):
        if flat_map[i] == 0 and flat_map[i-1] == 1 and flat_map[i+1] == 1:
            return i

my_id = find_my_seat(seat_map)
print(f'Part 1:\nMax seat ID: {max(seat_ids)}')
print(f'Part 2:\nMy seat ID: {my_id}')
