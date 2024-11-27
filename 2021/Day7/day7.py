
def read_input(file_loc):
    with open(file_loc, "r") as f:
        return [int(x) for x in f.read().split(",")]

positions = read_input("../Inputs/day7.txt")

def calc_total_fuel(positions, destination):
    return sum([abs(pos - destination) for pos in positions])

def calc_fuel_part_2(steps):
    steps = steps + 1
    return (steps * (steps - 1)) / 2

def calc_total_fuel_2(positions, destination):
    x = [calc_fuel_part_2(abs(pos - destination)) for pos in positions]
    return sum([calc_fuel_part_2(abs(pos - destination)) for pos in positions])

costs = []
smallest_pos = min(positions)
largest_pos = max(positions)

for i in range(smallest_pos, largest_pos + 1):
    costs.append(calc_total_fuel_2(positions, i))

min_cost = min(costs)

print(f'Part 1: {min_cost}')