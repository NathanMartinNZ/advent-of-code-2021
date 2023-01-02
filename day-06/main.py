
with open("input.txt") as f:
    fish = [int(fish) for fish in f.readline().split(",")]

### Part 1 & 2 ###
def calc_fish_count(days):
    fish_count = {key: fish.count(key) for key in range(9)}

    for _ in range(days):
        new_fish_count = {key: fish_count[key+1] if key != 8 else fish_count[0] for key in range(9)}
        new_fish_count[6] += fish_count[0]
        fish_count = new_fish_count
    
    return sum(fish_count.values())

part_1_answer = calc_fish_count(80)
print(part_1_answer)

part_2_answer = calc_fish_count(256)
print(part_2_answer)
