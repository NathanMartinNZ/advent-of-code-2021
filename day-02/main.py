import math

with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.replace("\n", "").split(" ") for line in lines]
    lines = [[x, int(y)] for x, y in lines]


### PART 1 ###
pos = [0, 0]

for command in lines:
    match command[0]:
        case "forward":
            pos[0] += command[1]
        case "up":
            pos[1] -= command[1]
        case "down":
            pos[1] += command[1]

part_1_answer = math.prod(pos)
print(part_1_answer)


### PART 2 ###
pos = [0, 0]
aim = 0

for command in lines:
    match command[0]:
        case "forward":
            pos[0] += command[1]
            pos[1] += command[1] * aim
        case "up":
            aim -= command[1]
        case "down":
            aim += command[1]

part_2_answer = math.prod(pos)
print(part_2_answer)