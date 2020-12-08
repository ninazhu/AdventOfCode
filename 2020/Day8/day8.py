# What value is in the accumulator?

def read_input(file_loc):
    with open(file_loc, "r") as f:
        values = f.read().split('\n')
    return values

def get_next_instruction(instructions, ind, executed_indices, accum):
    if ind in executed_indices:
        return accum, 1, executed_indices
    elif ind >= len(instructions):    # Part 2
        return accum, 0, executed_indices
    executed_indices.append(ind)
    instruction = instructions[ind].split(" ")
    if instruction[0] == "acc":
        accum = accum + int(instruction[1])
        ind = ind + 1
    elif instruction[0] == "jmp":
        ind = ind + int(instruction[1])
    else:
        ind = ind + 1
    return get_next_instruction(instructions, ind, executed_indices, accum)

instructions = read_input("../Inputs/day8.txt")
accum = 0

res, status, inds = get_next_instruction(instructions, 0, [], 0)
print(f'Part 1:\nAccumulator value: {res}')

# Part 2:
for i in inds:
    if instructions[i].split(" ")[0] == 'jmp':
        instr_copy = instructions.copy()
        instr_copy[i] = instructions[i].replace("jmp", "nop")
        res, term_status, inds = get_next_instruction(instr_copy, 0, [], 0)
        if term_status == 0:
            print(f'Part 2:\nAccumulator value: {res}')
            break
    elif instructions[i].split(" ")[0] == 'nop':
        instr_copy = instructions.copy()
        instr_copy[i] = instructions[i].replace("nop", "jmp")
        res, term_status, inds = get_next_instruction(instr_copy, 0, [], 0)
        if term_status == 0:
            print(f'Part 2:\nAccumulator value: {res}')
            break
