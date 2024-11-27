def read_input(file_loc):
    with open(file_loc, "r") as f:
        return [x.split(' | ') for x in f.read().split("\n")]

signals = read_input("../Inputs/day8.txt")

length_unique_digit_mapping = {2: 1, 4: 4, 3: 7, 7: 8}

count = 0
for signal in signals:
    digits = signal[1].split(" ")
    for digit in digits:
        if length_unique_digit_mapping.get(len(digit)) is not None:
            count = count + 1

print(f'Part 1: {count}')

# Part 2

on_mapping = {
    str([1, 2, 3, 5, 6, 7]): 0,
    str([3, 6]): 1,
    str([1, 3, 4, 5, 7]): 2,
    str([1, 3, 4, 6, 7]): 3,
    str([2, 3, 4, 6]): 4,
    str([1, 2, 4, 6, 7]): 5,
    str([1, 2, 4, 5, 6, 7]): 6,
    str([1, 3, 6]): 7,
    str([1, 2, 3, 4, 5, 6, 7]): 8,
    str([1, 2, 3, 4, 6, 7]): 9 
}

def get_digit(decode_map, digit_chars):
    on_list = []
    for c in digit_chars:
        on_list.append(int(decode_map.get(c)) + 1)
    on_list.sort()
    return on_mapping.get(str(on_list))

total = 0
for signal in signals:
    patterns = [set(x) for x in signal[0].split(" ")]
    decoded_numbers = [{'a','b','c','d','e','f','g'}] * 7
    patterns.sort(key=len)
    
    # the char in 7 not in 1 is decoded_numbers[0]
    decoded_numbers[0] = (patterns[0]^patterns[1])&patterns[1]
    # decoded_numbers[2] and [5] are one of the two chars for 1
    decoded_numbers[2] = patterns[0]
    decoded_numbers[5] = patterns[0]
    # decoded_numbers[1] and [3] are the chars in 4 not in 1
    decoded_numbers[1] = (patterns[0]^patterns[2])&patterns[2]
    decoded_numbers[3] = (patterns[0]^patterns[2])&patterns[2]
    # remove the above chars in the decoded_numbers from the remaining decoded_numbers
    decoded_numbers[4] = decoded_numbers[4] - decoded_numbers[0] - decoded_numbers[1] - decoded_numbers[2] - decoded_numbers[3] - decoded_numbers[5]
    # decoded_numbers[6] = decoded_numbers[4] - decoded_numbers[0] - decoded_numbers[1] - decoded_numbers[2] - decoded_numbers[3] - decoded_numbers[5]
    
    # the 5 char pattern with both chars from pattern[0] is 3
    ind_3 = 0
    for i in range(3, 6):
        if patterns[0].issubset(patterns[i]):
            ind_3 = i
            decoded_numbers[6] = patterns[i] - patterns[1] - patterns[2]
            decoded_numbers[4] = decoded_numbers[4] - decoded_numbers[6]
            # 4 - 3 reveals decoded_number[1]
            decoded_numbers[1] = patterns[2] - patterns[i]
            decoded_numbers[3] = decoded_numbers[3] - decoded_numbers[1]
            break

    for i in range(3, 6):
        if i != ind_3 and not decoded_numbers[4].issubset(patterns[i]):
            decoded_numbers[2] = patterns[2] - patterns[i]
            decoded_numbers[5] = decoded_numbers[5] - decoded_numbers[2]
            break
    
    # convert decoded_numbers to a map
    decode_map = {}
    for ind, i in enumerate(decoded_numbers):
        decode_map[list(i)[0]] = str(ind)

    digits = signal[1].split(" ")
    num_string = ''
    for digit in digits:
        num = length_unique_digit_mapping.get(len(digit))
        if num is None:
            num = get_digit(decode_map, digit)
        num_string = num_string + str(num)
    total = total + int(num_string)

print(f'Part 2: {total}')