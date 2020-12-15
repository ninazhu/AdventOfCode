# what will be the 2020th number spoken?

def read_input(file_loc):
    with open(file_loc, "r") as f:
        return [int(i) for i in f.read().split(",")]

spoken = {}

def add_turn(num, turn):
    turns_for_num = spoken.get(num, 0)
    if turns_for_num == 0:
        spoken[num] = [turn]
    elif turns_for_num == 1:
        spoken[num].append(turn)
    else:
        spoken[num] = [turn, max(turns_for_num)]        

starting_nums = read_input("../Inputs/day15.txt")

turns = []
last_spoken = 0
for turn in range(30000000):
    if turn < len(starting_nums):
        num = starting_nums[turn]
        spoken[num] = [turn]
        last_spoken = num
        continue
    if len(spoken.get(last_spoken)) == 1:
        num = 0
        add_turn(num, turn)
        last_spoken = num
    else:
        most_recent = spoken[num][0]
        next_most_recent = spoken[num][1]
        num = most_recent - next_most_recent
        add_turn(num, turn)
        last_spoken = num
        
print(last_spoken)
