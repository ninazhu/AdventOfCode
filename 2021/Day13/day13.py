def read_input(file_loc):
    with open(file_loc, "r") as f:
        return [x.split('\n') for x in f.read().split("\n\n")]

instructions = read_input("../Inputs/day13.txt")
dots = instructions[0]
folds = [x.split('fold along ')[1] for x in instructions[1]]

def do_fold(dots, dim, loc):
    new_dots = set()
    if dim == 'y':
        for dot in dots:
            dot_split = dot.split(',')
            dot_x = int(dot_split[0])
            dot_y = int(dot_split[1])
            if dot_y > loc:
                new_y = loc - (dot_y - loc)
                new_dot = f'{dot_x},{new_y}'
                new_dots.add(new_dot)
            else:
                new_dots.add(dot)
    else:
        for dot in dots:
            dot_split = dot.split(',')
            dot_x = int(dot_split[0])
            dot_y = int(dot_split[1])
            if dot_x > loc:
                new_x = loc - (dot_x - loc)
                new_dot = f'{new_x},{dot_y}'
                new_dots.add(new_dot)
            else:
                new_dots.add(dot)
    return new_dots

# Part 1 - first fold only
fold = folds[0]
fold_split = fold.split('=')
dim = fold_split[0]
loc = int(fold_split[1])
new_dots = do_fold(dots, dim, loc)

print(f'Part 1: {len(new_dots)}')

# Part 2

new_dots = dots.copy()
max_x = 0
max_y = 0
for fold in folds:
    fold_split = fold.split('=')
    dim = fold_split[0]
    loc = int(fold_split[1])
    if dim == 'x':
        max_x = loc
    if dim == 'y':
        max_y = loc
    new_dots = do_fold(new_dots, dim, loc)

printout = t = [['.']*max_x for _ in range(max_y)]
for dot in new_dots:
    dot_split = dot.split(',')
    dot_x = int(dot_split[0])
    dot_y = int(dot_split[1])
    printout[dot_y][dot_x] = '#'

for line in printout:
    print(''.join(line))