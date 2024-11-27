def read_input(file_loc):
    with open(file_loc, "r") as f:
        return [list(map(int, x)) for x in f.read().split()]

report = read_input("../Inputs/day3.txt")
threshold = len(report) / 2

def get_gamma_digit(sum_of_ones):
    if sum_of_ones > threshold:
        return '1'
    return '0'

def get_opposite_digit(digit):
    if digit == '1':
        return '0'
    return '1'

def get_eligible_indices(eligible_list, digit, col):
    list_of_inds = []
    for ind, x in enumerate(eligible_list):
        if str(x[col]) == digit:
            list_of_inds.append(ind)
    return list_of_inds

sum_of_ones_by_col = [sum(x) for x in zip(*report)]
gamma = [get_gamma_digit(x) for x in sum_of_ones_by_col]
epsilon = [get_opposite_digit(x) for x in gamma]

gamma_num = int(''.join(gamma), 2)
epsilon_num = int(''.join(epsilon), 2)

print(f'Part 1: {gamma_num * epsilon_num}')


def get_oxy_digit(sum_of_ones, len):
    if sum_of_ones >= (len/2):
        return '1'
    return '0'

def get_co2_digit(sum_of_ones, len):
    zeros = len - sum_of_ones
    if zeros <= sum_of_ones:
        return '0'
    return '1'

eligible_list = report
col = 0
while len(eligible_list) > 1:
    print()
    sum_of_ones_by_col = [sum(x) for x in zip(*eligible_list)]
    x = get_oxy_digit(sum_of_ones_by_col[col], len(eligible_list))
    eligible_inds = get_eligible_indices(eligible_list, x, col)
    
    new_eligible_list = [eligible_list[i] for i in eligible_inds]
    eligible_list = new_eligible_list
    col = col + 1
oxy = int("".join(str(i) for i in eligible_list[0]),2)
print(oxy)

eligible_list = report
col = 0
while len(eligible_list) > 1:
    sum_of_ones_by_col = [sum(x) for x in zip(*eligible_list)]
    x = get_co2_digit(sum_of_ones_by_col[col], len(eligible_list))
    eligible_inds = get_eligible_indices(eligible_list, x, col)
    
    new_eligible_list = [eligible_list[i] for i in eligible_inds]
    eligible_list = new_eligible_list
    col = col + 1
co2 = int("".join(str(i) for i in eligible_list[0]),2)
print(co2)

print(f'Part 2: {oxy * co2}')