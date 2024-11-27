import re

def read_input(file_loc):
    with open(file_loc, "r") as f:
        return [x.split('\n') for x in f.read().split("\n\n")]

instructions = read_input("../Inputs/test.txt")
start = instructions[0][0]
pair_inserts = [x.split(' -> ') for x in instructions[1]]
print(start)
print(pair_inserts)

def insert_in_new_chars(new_char, new_chars):
    if isinstance(new_char, list):
        for c in new_char:
            if new_chars.get(c) is None:
                new_chars[c] = 1
            else:
                new_chars[c] += 1
    else:
        if new_chars.get(new_char) is None:
            new_chars[new_char] = 1
        else:
            new_chars[new_char] += 1

# steps = 40
# polymer = start
# new_chars = {}
# for step in range(0, steps):
#     print(step)
#     subpolymers = []
#     for pair_insert in pair_inserts:
#         pair = pair_insert[0]
#         repl_char = pair_insert[1]
#         inds = [m.start() for m in re.finditer(f'(?={pair})', polymer)]
#         for ind in inds:
#             insert_in_new_chars(repl_char, new_chars)
#             subpolymer = polymer[ind] + repl_char + polymer[ind+1]
#             subpolymers.append(subpolymer)
#     polymer = ' '.join(subpolymers)

steps = 1
polymer = start
new_chars = {}
subpolymers = []
subpolymer_to_new_char = {}
for step in range(0, steps):
    print(step)
    if not subpolymers:
        for pair_insert in pair_inserts:
            pair = pair_insert[0]
            repl_char = pair_insert[1]
            inds = [m.start() for m in re.finditer(f'(?={pair})', polymer)]
            for ind in inds:
                insert_in_new_chars(repl_char, new_chars)
                subpolymer = polymer[ind] + repl_char + polymer[ind+1]
                subpolymers.append(subpolymer)
    else:
        tmp_subpolymers = subpolymers.copy()
        for subpolymer in subpolymers:
            if subpolymer not in subpolymer_to_new_char.keys():
                for pair_insert in pair_inserts:
                    pair = pair_insert[0]
                    repl_char = pair_insert[1]
                    inds = [m.start() for m in re.finditer(f'(?={pair})', polymer)]
                    for ind in inds:
                        insert_in_new_chars(repl_char, new_chars)
                        tmp_subpolymer = polymer[ind] + repl_char + polymer[ind+1]
                        tmp_subpolymers.append(tmp_subpolymer)
                        if subpolymer not in subpolymer_to_new_char.keys():
                            subpolymer_to_new_char[subpolymer] = [repl_char]
                        else:
                            subpolymer_to_new_char[subpolymer].append(repl_char)
            else:
                insert_in_new_chars(subpolymer_to_new_char[subpolymer], new_chars)
        subpolymers = tmp_subpolymers
        print(subpolymers)

for s in start:
    insert_in_new_chars(s, new_chars)

most_common = max(new_chars, key=new_chars.get)
least_common = min(new_chars, key=new_chars.get)

print(f'{(new_chars[most_common]) - (new_chars[least_common])}')