
with open("input.txt") as f:
    lines = f.readlines()
    lines = [int(line.replace("\n", "")) for line in lines]


### PART 1 ###
increased_num = 0

for i, line in enumerate(lines[1:]):
    if line > lines[i]:
        increased_num += 1

part_1_answer = increased_num
print(part_1_answer)


### PART 2 ###
increased_num = 0

for i, line in enumerate(lines[3:]):
    if sum(lines[i+1:i+4]) > sum(lines[i:i+3]):
        increased_num += 1

part_2_answer = increased_num
print(part_2_answer)

