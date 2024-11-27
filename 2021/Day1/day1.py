
def read_input(file_loc):
    with open(file_loc, "r") as f:
        return f.read().split("\n")

lines = read_input("../Inputs/day1.txt")
prev_line = None
count = 0

for line in lines:
    if prev_line is not None:
        if int(line) > int(prev_line):
            count = count + 1        
    prev_line = line

print(f'Part 1: {count}')

count = 0
prev_sum = None
for x, y in enumerate(lines):
    if x == len(lines) - 2:
        break
    curr_sum = int(lines[x]) + int(lines[x+1]) + int(lines[x+2])
    if prev_sum is not None:
        if curr_sum > prev_sum:
            count = count + 1
    prev_sum = curr_sum

print(f'Part 2: {count}')
