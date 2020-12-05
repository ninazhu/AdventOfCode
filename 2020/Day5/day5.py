# What is the highest seat ID on a boarding pass?

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



total_rows = list(range(0, 128))
total_cols = list(range(0, 8))

values = read_input("../Inputs/day5.txt")

res = []

for val in values:
    row = get_num(val[:7], total_rows)
    col = get_num(val[-3:], total_cols)
    seat_id = row * 8  + col
    res.append(seat_id)

print(f'Max seat ID: {max(res)}')
