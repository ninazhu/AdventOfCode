# How many messages completely match rule 0?

import re

def read_input(file_loc):
    with open(file_loc, "r") as f:
        output = f.read().split("\n\n")
    return [i for i in output[0].split("\n")], [i for i in output[1].split()]

def create_rules_map(rules):
    rules_map = {}
    for rule in rules:
        rule_split = rule.split(": ")
        rules_map[int(rule_split[0])] = rule_split[1]
    return rules_map

rules, msgs = read_input("../Inputs/test.txt")
rules = create_rules_map(rules)

print(rules)
print(msgs)



# def check_rule(rule_num, msg):
    # rule_val = rules[rule_num]
    # # base case
    # match = re.search(r'([ab])', rule_val)
    # if match:
    #     rule_letter = match.group(0)
    #     if msg[0] == rule_letter:
    #         return True
    #     return False
    # if "|" in rule_val:
    #     split = rule_val.split(" | ")
    #     return check_rule(split[0], msg) or check_rule(split[1], msg)
    # rule_val = rule_val.split(" ")
    # rule_1 = int(rule_val[0])
    # rule_2 = int(rule_val[1])
    # return check_rule(rule_1, msg) and check_rule(rule_2, msg)

def get_rule_possibilities(rule_num, curr_string):
    print(f'rule_num: {rule_num}')
    print(f'curr_string: {curr_string}')
    poss = set()
    if " " not in str(rule_num):
        rule_val = rules.get(rule_num)
        print(rule_val)
        match = re.search(r'([ab])', rule_val)
        if match:
            rule_letter = match.group(0)
            curr_string = curr_string + rule_letter
            return curr_string
        if "|" in rule_val:
            split = rule_val.split(" | ")
            print("*** ")
            poss.add(get_rule_possibilities(split[0], curr_string))
            poss.add(get_rule_possibilities(split[1], curr_string))
        else:
            rule_1 = int(rule_val.split(" ")[0])
            rule_2 = int(rule_val.split(" ")[1])
            res_1 = get_rule_possibilities(rule_1, curr_string)
            res_2 = get_rule_possibilities(rule_2, curr_string)
            poss.add(res_1 and res_2)
    else:
        rule_1 = int(rule_num.split(" ")[0])
        rule_2 = int(rule_num.split(" ")[1])
        res_1 = get_rule_possibilities(rule_1, curr_string)
        res_2 = get_rule_possibilities(rule_2, curr_string)
        poss.add(res_1 and res_2)
    return poss

possibilities = get_rule_possibilities(0, "")
print(possibilities)

# count = 0
# for msg in msgs:
#     if check_rule(0, msg):
#         count = count + 1

# print(count)