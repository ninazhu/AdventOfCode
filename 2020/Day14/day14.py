# What is the sum of all values left in memory after it completes?

import itertools

memory = {}

def read_input(file_loc):
    with open(file_loc, "r") as f:
        return f.read().split("\n")

def apply_mask(value, mask_str):
    for ind, val in enumerate(mask_str):
        if val != 'X':
            if int(val) == 0:
                value &=~ (1 << ind)
            if int(val) == 1:
                value |= (1 << ind)
    return value

def initialize_addr(addr, value, mask):
    value = apply_mask(value, mask)
    memory[addr] = value

program = read_input("../Inputs/day14.txt")

addr = 0
mask = ''
for line in program:
    line_split = line.split(" = ")
    instr = line_split[0]
    value = line_split[1]
    if instr == 'mask':
        mask = value[::-1]
    else:
        addr = instr[4:(len(instr) - 1)]
        initialize_addr(addr, int(value), mask)

print(f'Part 1:\n Sum of values in memory: {sum(memory.values())}')

# part 2

memory = {}

def apply_floating_inds(floating_inds, base_addr):
    combos = list(map(list, itertools.product([0, 1], repeat=len(floating_inds))))
    addrs = []
    for c in combos:
        new_addr = base_addr
        for i, val in enumerate(c):
            new_addr &=~ (1 << floating_inds[i])
            new_addr |= (val << floating_inds[i])
        addrs.append(new_addr)
    return addrs

def get_addrs(addr, mask_str):
    floating_inds = []
    for ind, val in enumerate(mask_str):
        if val == '0':
            continue
        elif val == '1':
            addr |= (1 << ind)
        elif val == 'X':
            floating_inds.append(ind)
    addrs = apply_floating_inds(floating_inds, addr)
    return addrs

for line in program:
    line_split = line.split(" = ")
    instr = line_split[0]
    value = line_split[1]
    if instr == 'mask':
        mask = value[::-1]
        continue
    else:
        addr = instr[4:(len(instr) - 1)]
        addrs = get_addrs(int(addr), mask)
    for a in addrs:
        memory[a] = int(value)

print(f'Part 2:\n Sum of values in memory: {sum(memory.values())}')
