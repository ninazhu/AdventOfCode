# How many seats end up occupied?

from pprint import pprint

def read_input(file_loc):
    with open(file_loc, "r") as f:
        return [list(i.strip()) for i in f]

seat_map = read_input("../Inputs/day11.txt")

def get_num_neighbors(i, j, seats):
    num = 0
    height = len(seats) - 1
    width = len(seats[0]) - 1

    if i > 0 and j > 0:    
        if seats[i-1][j-1] == '#':
            num = num + 1
    if i > 0:   
        if seats[i-1][j] == '#':
            num = num + 1
    if i > 0 and j < width:
        if seats[i-1][j+1] == '#':
            num = num + 1
    if j > 0:
        if seats[i][j-1] == '#':
            num = num + 1
    if j < width:
        if seats[i][j+1] == '#':
            num = num + 1
    if i < height and j > 0:
        if seats[i+1][j-1] == '#':
            num = num + 1
    if i < height:
        if seats[i+1][j] == '#':
            num = num + 1
    if i < height and j < width:
        if seats[i+1][j+1] == '#':
            num = num + 1
    return num

def get_num_neighbors_2(i, j, seats):
    num = 0
    height = len(seats) - 1
    width = len(seats[0]) - 1
    
    # look up
    i_sub = i
    j_sub = j
    while i_sub > 0:
        if seats[i_sub-1][j] == '#':
            num = num + 1
            break
        elif seats[i_sub-1][j] == 'L':
            break
        i_sub = i_sub - 1
    # look down
    i_sub = i
    j_sub = j
    while i_sub < height:
        if seats[i_sub+1][j] == '#':
            num = num + 1
            break
        elif seats[i_sub+1][j] == 'L':
            break
        i_sub = i_sub + 1
    # look left
    i_sub = i
    j_sub = j
    while j_sub > 0:
        if seats[i][j_sub-1] == '#':
            num = num + 1
            break
        elif seats[i][j_sub-1] == 'L':
            break
        j_sub = j_sub - 1
    # look right
    i_sub = i
    j_sub = j
    while j_sub < width:
        if seats[i][j_sub+1] == '#':
            num = num + 1
            break
        elif seats[i][j_sub+1] == 'L':
            break
        j_sub = j_sub + 1
    # look up-left
    i_sub = i
    j_sub = j
    while i_sub > 0 and j_sub > 0:
        if seats[i_sub-1][j_sub-1] == '#':
            num = num + 1
            break
        elif seats[i_sub-1][j_sub-1] == 'L':
            break
        i_sub = i_sub - 1
        j_sub = j_sub - 1
    # look up-right
    i_sub = i
    j_sub = j
    while i_sub > 0 and j_sub < width:
        if seats[i_sub-1][j_sub+1] == '#':
            num = num + 1
            break
        elif seats[i_sub-1][j_sub+1] == 'L':
            break
        i_sub = i_sub - 1
        j_sub = j_sub + 1
    # look down-left
    i_sub = i
    j_sub = j
    while i_sub < height and j_sub > 0:
        if seats[i_sub+1][j_sub-1] == '#':
            num = num + 1
            break
        elif seats[i_sub+1][j_sub-1] == 'L':
            break
        i_sub = i_sub + 1
        j_sub = j_sub - 1
    # look down-right
    i_sub = i
    j_sub = j
    while i_sub < height and j_sub < width:
        if seats[i_sub+1][j_sub+1] == '#':
            num = num + 1
            break
        elif seats[i_sub+1][j_sub+1] == 'L':
            break
        i_sub = i_sub + 1
        j_sub = j_sub + 1
    return num

def get_next_round_seat_map(curr_seat_map):
    next_round_map = [row[:] for row in curr_seat_map]
    for i, row in enumerate(curr_seat_map):
        for j, seat in enumerate(row):
            if seat == 'L':
                occupied_neighbors = get_num_neighbors_2(i, j, curr_seat_map)
                if occupied_neighbors == 0:
                    next_round_map[i][j] = '#'
            elif seat == '#':
                occupied_neighbors = get_num_neighbors_2(i, j, curr_seat_map)
                if occupied_neighbors >= 5:
                    next_round_map[i][j] = 'L'
    return next_round_map

curr_seat_map = [row[:] for row in seat_map]
next_round_map = get_next_round_seat_map(curr_seat_map)

while next_round_map != curr_seat_map:
    curr_seat_map = [row[:] for row in next_round_map]
    next_round_map = get_next_round_seat_map(curr_seat_map)

print(f'Filled seats: {sum(row.count("#") for row in next_round_map)}')
