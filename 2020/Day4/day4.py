# In your batch file, how many passports are valid?

import re

def read_input(file_loc):
    with open(file_loc, "r") as f:
        values = f.read().split('\n\n')
    values = [{x.split(':')[0]: x.split(':')[1] for x in i.split()} for i in values]
    return values

def is_valid_value(field, value):
    if value is None:
        return False
    if not validate_field_values:
        return True
    try:
        if field == 'byr':
            return 1920 <= int(value) <= 2002
        elif field == 'iyr':
            return 2010 <= int(value) <= 2020
        elif field == 'eyr':
            return 2020 <= int(value) <= 2030
        elif field == 'hgt':
            matches = re.search(r'\A(\d+)(cm|in){1}\Z', value)
            if matches.group(2) == 'cm':
                return 150 <= int(matches.group(1)) <= 193
            if matches.group(2) == 'in':
                return 59 <= int(matches.group(1)) <= 76
        elif field == 'hcl':
            matches = re.search(r'\A#([0-9a-f]{6})\Z', value)
            return matches is not None
        elif field == 'ecl':
            return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif field == 'pid':
            matches = re.search(r'\A\d{9}\Z', value)
            return matches is not None
    except:
        return False

def is_valid(passport):
    for f in required_fields:
        if not is_valid_value(f, passport.get(f)):
            return False
    return True

# to toggle between Part 1 (False) and Part 2 (True)
validate_field_values = True
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_passports = 0

values = read_input("../Inputs/day4.txt")
for passport in values:
    if is_valid(passport):
        valid_passports = valid_passports + 1

print(f'Valid Passports: {valid_passports}')
