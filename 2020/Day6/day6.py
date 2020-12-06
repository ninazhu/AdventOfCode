# What is the sum of those counts?

def read_input(file_loc):
    with open(file_loc, "r") as f:
        values = f.read().split('\n\n')
    values = [i for i in values]
    return values

groups = read_input("../Inputs/day6.txt")
total_count_1 = 0
total_count_2 = 0
for group in groups:
    total_ans = group.replace('\n', '')
    unique_ans = set(list(total_ans))
    total_count_1 = total_count_1 + len(unique_ans)

    # for part 2
    individuals = [list(x) for x in group.split('\n')]
    overlap = len(set.intersection(*map(set, individuals)))
    total_count_2 = total_count_2 + overlap

print(f'Part 1:\nTotal count: {total_count_1}')
print(f'Part 2:\nTotal count: {total_count_2}')
