def read_input(file_loc):
    with open(file_loc, "r") as f:
        return f.read().split("\n\n")

lines = read_input("../Inputs/day4.txt")

numbers = None
boards = []
board_marks = []
for ln_count, ln in enumerate(lines):
    if ln_count == 0:
        numbers = ln.split(',')
    else:
        boards.append(ln.split())
        board_marks.append([0] * 25)

win_sequence = []   # for part 2
win_sequence_num = []
win_sequence_scores = []

def is_new_winning_board(board_mark, board_num):
    if board_num in win_sequence:
        return False
    if sum(board_mark[:5]) == 5 or sum(board_mark[5:10]) == 5 \
            or sum(board_mark[10:15]) == 5 or sum(board_mark[15:20]) == 5 \
            or sum(board_mark[20:25]) == 5:
        return True
    if (board_mark[0] + board_mark[5] + board_mark[10] + board_mark[15] + board_mark[20]) == 5 or \
            (board_mark[1] + board_mark[6] + board_mark[11] + board_mark[16] + board_mark[21]) == 5 or \
            (board_mark[2] + board_mark[7] + board_mark[12] + board_mark[17] + board_mark[22]) == 5 or \
            (board_mark[3] + board_mark[8] + board_mark[13] + board_mark[18] + board_mark[23]) == 5 or \
            (board_mark[4] + board_mark[9] + board_mark[14] + board_mark[19] + board_mark[24]) == 5:
        return True
    return False

first_winning_board = None
first_winning_board_last_num = None

def calculate_final_score(place):
    sum_unmarked = 0
    for ind, number in enumerate(boards[win_sequence[place]]):
        if board_marks[win_sequence[place]][ind] == 0:
            sum_unmarked = sum_unmarked + int(number)
    return sum_unmarked * int(win_sequence_num[place])

for number in numbers:
    # mark the boards
    for board_num, board in enumerate(boards):
        if number in board:
            ind = board.index(number)
            board_marks[board_num][ind] = 1
        # check if board won
        if is_new_winning_board(board_marks[board_num], board_num):
            win_sequence.append(board_num)
            win_sequence_num.append(number)
            win_sequence_scores.append(calculate_final_score(len(win_sequence) - 1))
    if len(win_sequence) == len(boards):
        break
    
print(f'Part 1: {win_sequence_scores[0]}')
print(f'Part 2: {win_sequence_scores[len(win_sequence) - 1]}')