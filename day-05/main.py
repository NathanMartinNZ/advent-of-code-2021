
with open("input.txt") as f:
    vents = [[int(val) for val in line.replace("\n", "").replace(" -> ", ",").split(",")] for line in f.readlines()]

### Part 1 & 2 ###
num_x = 0
num_y = 0
for line in vents:
    if line[0] > num_x: num_x = line[0]
    if line[2] > num_x: num_x = line[2]
    if line[1] > num_y: num_y = line[1]
    if line[3] > num_y: num_y = line[3]


def draw_vents(only_straight_lines):
    map = [[0 for _ in range(num_x+1)] for _ in range(num_y+1)]

    for vent in vents:
        x_length = vent[2] - vent[0] if vent[2] >= vent[0] else vent[0] - vent[2]
        y_length = vent[3] - vent[1] if vent[3] >= vent[1] else vent[1] - vent[3]

        vals_to_draw = max([x_length, y_length]) + 1

        for idx in range(vals_to_draw):
            x_draw, y_draw = vent[0], vent[1]
            if x_length > 0:
                x_draw = abs(vent[0] - idx) if vent[0] > vent[2] else abs(vent[0] + idx)
            if y_length > 0:
                y_draw = abs(vent[1] - idx) if vent[1] > vent[3] else abs(vent[1] + idx)

            if only_straight_lines and x_length > 0 and y_length > 0:
                break
            
            map[y_draw][x_draw] += 1
    
    return sum([sum([1 for val in row if val >= 2]) for row in map])


part_1_answer = draw_vents(True) # only_straight_lines
print(f"Part 1: {part_1_answer}")

part_2_answer = draw_vents(False) # incl. horizontal
print(f"Part 2: {part_2_answer}")