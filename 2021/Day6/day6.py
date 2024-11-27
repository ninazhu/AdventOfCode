
def read_input(file_loc):
    with open(file_loc, "r") as f:
        return [int(x) for x in f.read().split(",")]

fish = read_input("../Inputs/day6.txt")

counts = {}
for i in fish:
  counts[i] = counts.get(i, 0) + 1

days = 256
for i in range(0, days):
    if i % 25 == 0:
        print(i)
    counts_8 = counts.get(8, 0)
    counts_7 = counts.get(7, 0)
    counts_6 = counts.get(6, 0)
    counts_5 = counts.get(5, 0)
    counts_4 = counts.get(4, 0)
    counts_3 = counts.get(3, 0)
    counts_2 = counts.get(2, 0)
    counts_1 = counts.get(1, 0)
    counts_0 = counts.get(0, 0)
    counts[8] = counts_0
    counts[7] = counts_8
    counts[6] = counts_7 + counts_0
    counts[5] = counts_6
    counts[4] = counts_5
    counts[3] = counts_4
    counts[2] = counts_3
    counts[1] = counts_2
    counts[0] = counts_1

print(sum(counts.values()))
