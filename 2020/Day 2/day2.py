# How many passwords are valid according to their policies?

def read_input(file_loc):
    with open(file_loc, "r") as f:
        values = f.read().split('\n')
    values = [i.split(': ') for i in values]
    return values

# for part 1
def pw_is_valid(rule_min, rule_max, rule_char, pw):
    count = pw.count(rule_char)
    if rule_min <= count <= rule_max:
        return True
    return False

# for part 2
def pw_is_valid_2(pos_1, pos_2, rule_char, pw):
    if (pw[pos_1 - 1] == rule_char) ^ (pw[pos_2 - 1] == rule_char):
        return True
    return False

values = read_input("../Inputs/day2.txt")
valid_pws = 0
valid_pws_2 = 0

for [rule, pw] in values:
    [rule_min_max, rule_char] = rule.split(" ")
    [rule_min, rule_max] = rule_min_max.split("-")
    if pw_is_valid(int(rule_min), int(rule_max), rule_char, pw):
        valid_pws = valid_pws + 1
    if pw_is_valid_2(int(rule_min), int(rule_max), rule_char, pw):
        valid_pws_2 = valid_pws_2 + 1

print(f'Part 1:\nNumber of valid passwords: {valid_pws}')
print(f'Part 2:\nNumber of valid passwords: {valid_pws_2}')
