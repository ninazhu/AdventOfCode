# What value is in the accumulator?

def read_input(file_loc):
    with open(file_loc, "r") as f:
        values = f.read().split('\n')
    return values

def get_next_instruction(instructions, ind, executed_indices, accum):
    if ind in executed_indices:
        return accum
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
executed_indices = []
accum = 0

result = get_next_instruction(instructions, 0, executed_indices, 0)
print(f'Part 1:\nAccumulator value: {result}')
