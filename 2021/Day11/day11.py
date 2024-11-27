def read_input(file_loc):
    with open(file_loc, "r") as f:
        return f.read().split("\n")

octo_map = read_input("../Inputs/day11.txt")

height = len(octo_map)
width = len(octo_map[0])
flatmap = [int(x) for x in ''.join(octo_map)]

def get_upper(ind):
    if ind < width:
        return None, None
    return flatmap[ind-width], ind-width

def get_lower(ind):
    if ind > len(flatmap) - width - 1:
        return None, None
    return flatmap[ind+width], ind+width

def get_left(ind):
    if ind % width == 0:
        return None, None
    return flatmap[ind - 1], ind - 1

def get_right(ind):
    if (ind + 1) % width == 0:
        return None, None
    return flatmap[ind + 1], ind + 1

def get_upper_left(ind):
    if ind < width or ind % width == 0:
        return None, None
    return flatmap[ind - width - 1], ind - width - 1

def get_upper_right(ind):
    if ind < width or ((ind + 1) % width == 0):
        return None, None
    return flatmap[ind - width + 1], ind - width + 1

def get_lower_left(ind):
    if (ind > len(flatmap) - width - 1) or ind % width == 0:
        return None, None
    return flatmap[ind + width - 1], ind + width - 1

def get_lower_right(ind):
    if (ind > len(flatmap) - width - 1) or (ind + 1) % width == 0:
        return None, None
    return flatmap[ind+width+1], ind+width+1

def flash(ind, already_flashed):
    # print(f'{flatmap[ind]} at ind {ind}')
    # print(already_flashed)
    # print(f'flatmap: {flatmap}')
    flatmap[ind] = 0
    already_flashed.append(ind)
    upper, upper_ind = get_upper(ind)
    lower, lower_ind = get_lower(ind)
    left, left_ind = get_left(ind)
    right, right_ind = get_right(ind)
    upper_left, upper_left_ind = get_upper_left(ind)
    upper_right, upper_right_ind = get_upper_right(ind)
    lower_left, lower_left_ind = get_lower_left(ind)
    lower_right, lower_right_ind = get_lower_right(ind)
    # print(f'{upper} {lower} {left} {right} {upper_left} {upper_right} {lower_left} {lower_right}')
    # increase adjacents by 1
    if upper_ind is not None and upper_ind not in already_flashed:
        flatmap[upper_ind] = upper + 1
    if lower_ind is not None and lower_ind not in already_flashed:
        flatmap[lower_ind] = lower + 1
    if left_ind is not None and left_ind not in already_flashed:
        flatmap[left_ind] = left + 1
    if right_ind is not None and right_ind not in already_flashed:
        flatmap[right_ind] = right + 1
    if upper_left_ind is not None and upper_left_ind not in already_flashed:
        flatmap[upper_left_ind] = upper_left + 1
    if upper_right_ind is not None and upper_right_ind not in already_flashed:
        flatmap[upper_right_ind] = upper_right + 1
    if lower_left_ind is not None and lower_left_ind not in already_flashed:
        flatmap[lower_left_ind] = lower_left + 1
    if lower_right_ind is not None and lower_right_ind not in already_flashed:
        flatmap[lower_right_ind] = lower_right + 1
    # flash
    if upper_ind is not None and upper_ind not in already_flashed:
        if flatmap[upper_ind] > 9:
            already_flashed = flash(upper_ind, already_flashed)
    if lower_ind is not None and lower_ind not in already_flashed:
        if flatmap[lower_ind] > 9:
            already_flashed = flash(lower_ind, already_flashed)
    if left_ind is not None and left_ind not in already_flashed:
        if flatmap[left_ind] > 9:
            already_flashed = flash(left_ind, already_flashed)
    if right_ind is not None and right_ind not in already_flashed:
        if flatmap[right_ind] > 9:
            already_flashed = flash(right_ind, already_flashed)
    if upper_left_ind is not None and upper_left_ind not in already_flashed:
        if flatmap[upper_left_ind] > 9:
            already_flashed = flash(upper_left_ind, already_flashed)
    if upper_right_ind is not None and upper_right_ind not in already_flashed:
        if flatmap[upper_right_ind] > 9:
            already_flashed = flash(upper_right_ind, already_flashed)
    if lower_left_ind is not None and lower_left_ind not in already_flashed:
        if flatmap[lower_left_ind] > 9:
            already_flashed = flash(lower_left_ind, already_flashed)
    if lower_right_ind is not None and lower_right_ind not in already_flashed:
        if flatmap[lower_right_ind] > 9:
            already_flashed = flash(lower_right_ind, already_flashed)

    return already_flashed

num_steps = 500
total_flashes = 0
for step in range(0, num_steps):
    # print(f'{step}: {flatmap}')
    # increment all by 1
    flatmap = [i + 1 for i in flatmap]
    # do flashes
    already_flashed = []
    for ind, octopus in enumerate(flatmap):
        if octopus > 9:
            already_flashed = flash(ind, already_flashed)
    if len(set(already_flashed)) == len(flatmap):
        print(f'Part 2: step {step + 1}')
        break
    total_flashes += len(already_flashed)
    # print(flatmap)

print(f'Part 1: {total_flashes}')
