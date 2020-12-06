# What is the sum of those counts?

def read_input(file_loc):
    with open(file_loc, "r") as f:
        values = f.read().split('\n\n')
    values = [i for i in values]
    return values

groups = read_input("../Inputs/day6.txt")
total_count = 0
for group in groups:
    total_ans = group.replace('\n', '')
    unique_ans = set(list(total_ans))
    total_count = total_count + len(unique_ans)

print(f'Part 1:\nTotal count: {total_count}')
