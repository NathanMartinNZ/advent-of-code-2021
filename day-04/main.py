
with open("input.txt") as f:
    lines = f.readlines()
    numbers = [int(n) for n in lines[0].split(",")]

    boards = [[] for line in lines[1:] if line == "\n"]

    board_num = 0
    for line in lines[2:]:
        if line == "\n":
            board_num += 1
        else:
            row = line.replace("\n", "").strip().replace("  ", " ").split(" ")
            row = [[int(num), False] for num in row] # [number, numberWasDrawn]
            boards[board_num].append(row)
    

### PART 1 & 2 ###
first_winner_score = 0
winners = [] # [[board_idx, drawnNumberToWin]]

def mark_board(board, drawn_num):
    for row in board:
        for num in row:
            if num[0] == drawn_num:
                num[1] = True

def check_if_won(board, board_idx):
    # Check rows
    for row in board:
        winning_nums = sum([1 for num in row if num[1] == True])
        if winning_nums == 5:
            return board_idx

    # Check cols
    for row in list(map(list, zip(*board))): # Transpose board
        winning_nums = sum([1 for num in row if num[1] == True])
        if winning_nums == 5:
            return board_idx

    return -1

def calc_score(board, lastDrawnNumber):
    unmarked_sum = 0
    for row in board:
        unmarked_sum += sum([num[0] for num in row if num[1] == False])

    return unmarked_sum * lastDrawnNumber

for number in numbers:
    for idx, board in enumerate(boards):
        not_yet_won = all(winner[0] != idx for winner in winners)
        if not_yet_won:
            mark_board(board, number)
    
    for idx, board in enumerate(boards):
        won = check_if_won(board, idx) >= 0
        not_yet_won = all(winner[0] != idx for winner in winners)
        if won and not_yet_won:
            winners.append([idx, number])


part_1_answer = calc_score(boards[winners[0][0]], winners[0][1])
print(part_1_answer)

part_2_answer = calc_score(boards[winners[-1][0]], winners[-1][1])
print(part_2_answer)