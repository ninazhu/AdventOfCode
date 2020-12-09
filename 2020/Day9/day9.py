# What is the first number that does not have this property?

def read_input(file_loc):
    with open(file_loc, "r") as f:
        values = f.read().split('\n')
    values = [int(i) for i in values]
    return values

def has_2_nums(value, input_nums):
    # print(value, str(input_nums))
    input_copy = input_nums.copy()
    for num in input_nums:
        input_copy.remove(num)
        if value-num in input_nums:
            return True
    return False

def find_sum(curr_sum, curr_ind):
    if curr_sum + values[curr_ind] >= invalid_val:
        return curr_sum + values[curr_ind], curr_ind
    return find_sum(curr_sum + values[curr_ind], curr_ind+1)

values = read_input("../Inputs/day9.txt")
preamble_length = 25
invalid_val = 0
invalid_ind = 0
for i in range(preamble_length, len(values)):
    # print(values[i])
    if not has_2_nums(values[i], values[i-preamble_length:i]):
        invalid_val = values[i]
        invalid_ind = i
        break

print(f'Part 1:\nInvalid value: {invalid_val}')

# part 2
start_ind = 0
end_ind = 0
for i in range(0, invalid_ind):
    sum, ind = find_sum(0, i)
    if sum == invalid_val:
        start_ind = i 
        end_ind = ind
        break

sub_list = values[start_ind:end_ind]
min_val = min(sub_list)
max_val = max(sub_list)
print(f'Part 2:\n{min_val+ max_val}')
