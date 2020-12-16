# What is your ticket scanning error rate?

import collections
import pandas as pd

def read_input(file_loc):
    with open(file_loc, "r") as f:
        return f.read().split("\n\n")

def parse_rule(rule):
    rule_vals = []
    rule_split = rule.split(" or ")
    left_rule = rule_split[0].split("-")
    right_rule = rule_split[1].split("-")
    rule_vals = list(range(int(left_rule[0]), int(left_rule[1]) + 1))
    rule_vals = rule_vals + list(range(int(right_rule[0]), int(right_rule[1]) + 1))
    return rule_vals

def parse_fields(field_list):
    fields = {}
    for line in field_list:
        line_split = line.split(": ")
        fields[line_split[0]] = parse_rule(line_split[1])
    return fields

def parse_tickets(ticket_list):
    return [
        [int(i) for i in line.split(",")]
        for line in ticket_list
        if "," in line
    ]

def get_all_valid_vals(fields):
    valid_vals = set()
    for vals in fields.values():
        valid_vals.update(set(vals))
    return valid_vals

notes = read_input("../Inputs/day16.txt")

fields = parse_fields(notes[0].split("\n"))
my_ticket = parse_tickets(notes[1].split("\n"))[0]
nearby_tickets = parse_tickets(notes[2].split("\n"))

all_valid_vals = get_all_valid_vals(fields)
sum_invalid_vals = 0
valid_tickets = []
for ticket in nearby_tickets:
    is_valid_ticket = True
    for val in ticket:
        if val not in all_valid_vals:
            sum_invalid_vals = sum_invalid_vals + val
            is_valid_ticket = False
    if is_valid_ticket:
        valid_tickets.append(ticket)

valid_tickets = pd.DataFrame(valid_tickets)
possible_cols = {}
for col in valid_tickets:
    possible_cols[col] = []
    for field, valid_vals in fields.items():
        if set(valid_tickets[col]) - set(valid_vals) == set():
            possible_cols[col].append(field)

final_cols = list(range(len(my_ticket)))
possible_cols = collections.OrderedDict(
    sorted(possible_cols.items(), key=lambda x: len(x[1]))
)
for k, fields in possible_cols.items():
    f = [i for i in fields if i not in final_cols]
    final_cols[k] = f[0]

product = 1
for i, col in enumerate(final_cols):
    if col.startswith("departure"):
        product = product * my_ticket[i]

print(f'Part 1:\n Sum of invalid values: {sum_invalid_vals}')
print(f'Part 2:\n Product of departure values: {product}')
