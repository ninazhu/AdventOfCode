# Evaluate the expression on each line of the homework; what is the sum of the resulting values?

import re

def read_input(file_loc):
    with open(file_loc, "r") as f:
        return f.read().split("\n")

def do_math(line):
    line = line.split(" ")
    val = int(line[0])
    line = line[1:]
    for i, x in enumerate(line[::2]):
        if x == '+':
            val = val + int(line[i*2 + 1])
        elif x == '*':
            val = val * int(line[i*2 + 1])
    return val

def do_math_2(line):
    if "+" not in line:
        return eval(line)
    match = re.sub(
        r'(\d+ \+ \d+)',
        lambda x: str(eval(x.group(1))),
        line
    )
    return do_math_2(match)

hw = read_input("../Inputs/day18.txt")
results = []
for line in hw:
    while '(' in line:
        line = re.sub(
            r'\(([\d\+\* ]+)\)',
            lambda x: str(do_math(x.group(1))),
            line
        )
    results.append(do_math(line))

print(f'Part 1:\n Sum of answers: {sum(results)}')

results_2 = []
for line in hw:
    while '(' in line:
        line = re.sub(
            r'\(([\d\+\* ]+)\)',
            lambda x: str(do_math_2(x.group(1))),
            line
        )
    results_2.append(do_math_2(line))

print(f'Part 2:\n Sum of answers: {sum(results_2)}')
