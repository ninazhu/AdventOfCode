# What is the ID of the earliest bus you can take to the airport
# multiplied by the number of minutes you'll need to wait for that bus?

import math

def read_input(file_loc):
    with open(file_loc, "r") as f:
        return f.read().split("\n")

notes = read_input("../Inputs/day13.txt")
earliest_time = int(notes[0])
busses = [int(i) for i in notes[1].split(",") if i != "x"]

schedule = {}
for bus in busses:
    next_time = (math.floor(earliest_time / bus) + 1) * bus
    schedule[next_time] = bus

min_waiting = min(schedule) - earliest_time
earliest_bus = schedule.get(min(schedule))
print(f"Part 1:\n ID x minutes waiting: {min_waiting * earliest_bus}")

# Part 2

def lcm(a, b):
    return int(abs(a * b) / math.gcd(a, b))

t = 0
multiplier = 1
for offset, bus in enumerate(notes[1].split(',')):
    if bus == 'x':
        continue
    bus = int(bus)
    while (t + offset) % bus != 0:
        t = t + multiplier
    multiplier = lcm(bus, multiplier)

print(f"Part 2:\n Earliest Time: {t}")
