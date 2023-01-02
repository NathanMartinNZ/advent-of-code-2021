
with open("input.txt") as f:
    h_positions = [int(position) for position in f.readline().split(",")]

### Part 1 & 2 ###
def calc_optimal_fuel(part):
    fuel_used = 0

    for position_target in range(min(h_positions), max(h_positions)):
        fuel_used_for_position = 0

        for position in h_positions:
            if part == 1:
                fuel_used_for_position += abs(position - position_target)
            else:
                fuel_used_for_position += abs(position - position_target) * (abs(position - position_target) + 1) // 2

        if fuel_used == 0:
            fuel_used = fuel_used_for_position
        elif fuel_used_for_position <= fuel_used:
            fuel_used = fuel_used_for_position
        else:
            break

    return fuel_used 

part_1_answer = calc_optimal_fuel(1)
print(part_1_answer)

part_2_answer = calc_optimal_fuel(2)
print(part_2_answer)