def read_input(file_loc):
    with open(file_loc, "r") as f:
        return f.read().split("\n")

subsystem = read_input("../Inputs/day10.txt")

open_to_close_map = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

illegal_char_cost = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

completion_char_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def remove_pairs(line):
    new_line = line
    new_line = new_line.replace('()', '')
    new_line = new_line.replace('{}', '')
    new_line = new_line.replace('[]', '')
    new_line = new_line.replace('<>', '')
    if new_line != line:
        return remove_pairs(new_line)
    else:
        return new_line

# find illegal characters
syntax_error_score = 0
incomplete_lines = []
for line in subsystem:
    # print(line)
    remaining_line = remove_pairs(line)
    incomplete_lines.append(remaining_line)
    for ind, char in enumerate(remaining_line):
        if char not in open_to_close_map.keys():
            prev_char = remaining_line[ind-1]
            exp_char = open_to_close_map[prev_char]
            # print(f'Expected {exp_char}, got {char}')
            syntax_error_score += illegal_char_cost[char]
            incomplete_lines.remove(remaining_line)
            break

print(f'Part 1: {syntax_error_score}')

list_total_scores = []
for ic_line in incomplete_lines:
    total_score = 0
    for char in ic_line[::-1]:
        total_score = (total_score * 5) + completion_char_points[open_to_close_map[char]]
    list_total_scores.append(total_score)

list_total_scores.sort()
print(f'Part 2: {list_total_scores[int((len(list_total_scores) -1)/2)]}')
