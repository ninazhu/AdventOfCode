# How many bag colors can eventually contain at least one shiny gold bag?

def read_input(file_loc):
    with open(file_loc, "r") as f:
        values = f.read().split('\n')
    return values

def build_child_to_parent_rules(values):
    result = {}
    for value in values:
        bag_type = value.split(' bags contain ')[0]
        contents = value.split(' bags contain ')[1]
        # config = {}
        for content in contents.split(', '):
            content = content.replace(" bags", "")
            content = content.replace(" bag", "")
            content = content.replace(".", "")
            num = content.split(" ")[0]
            if num == "no":
                continue
            child_type = "".join(content[2:])
            if result.get(child_type) is None:
                result[child_type] = {bag_type: int(num)}
            else:
                result[child_type][bag_type] = int(num)
    return result

def build_parent_to_child_rules(values):
    result = {}
    for value in values:
        parent_type = value.split(' bags contain ')[0]
        child_types = value.split(' bags contain ')[1]
        config = {}
        for child in child_types.split(', '):
            child = child.replace(" bags", "")
            child = child.replace(" bag", "")
            child = child.replace(".", "")
            if child == "no other":
                continue
            num = int(child.split(" ")[0])
            config["".join(child[2:])] = num
        result[parent_type] = config
    return result

def get_parent_colors(input_color, rules):
    colors = set()
    if rules.get(input_color) is None:
        return colors
    for color in rules[input_color]:
        colors.add(color)
        colors |= get_parent_colors(color, rules)
    return colors

def get_num_bags(input_color, rules):
    count = 0
    if rules.get(input_color) == {}:
        return count
    for color in rules[input_color]:
        child_count = rules[input_color][color]
        count = count + child_count
        count = count + child_count * get_num_bags(color, rules)
    return count

values = read_input("../Inputs/day7.txt")
my_color = 'shiny gold'

# Part 1
child_to_parent_rules = build_child_to_parent_rules(values)
colors = get_parent_colors(my_color, child_to_parent_rules)
print(f'Part 1:\nNumber of colors: {len(colors)}')

# Part 2
parent_to_child_rules = build_parent_to_child_rules(values)
count = get_num_bags(my_color, parent_to_child_rules)
print(f'Part 2:\nNumber of bags: {count}')
