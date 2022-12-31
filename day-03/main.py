
with open("input.txt") as f:
    lines = f.readlines()
    lines = [[int(x) for x in list(line.replace("\n", ""))] for line in lines]


### PART 1 ###
rate_list_count = [0 for _ in range(12)]

for line in lines:
    for i, bit in enumerate(line):
        rate_list_count[i] += 1 if bit == 1 else -1

gamma_rate = [1 if g>0 else 0 for g in rate_list_count]
epsilon_rate = [0 if e>0 else 1 for e in rate_list_count]

gamma_rate = int(''.join(str(b) for b in gamma_rate), 2)
epsilon_rate = int(''.join(str(b) for b in epsilon_rate), 2)

part_1_answer = gamma_rate * epsilon_rate
print(part_1_answer)


### PART 2 ###
lines = [{"number": i, "bits": line} for i, line in enumerate(lines)]

def calc_ratings(rating_type):
    lines_final = lines.copy()

    for bit_i in range(12):
        rate_list_count = [0 for _ in range(12)]

        for line in lines_final:
            for i, bit in enumerate(line["bits"]):
                rate_list_count[i] += 1 if bit == 1 else -1
        
        if rating_type == "oxygen":
            rate_list = [1 if o>=0 else 0 for o in rate_list_count]
        else:
            rate_list = [0 if o>=0 else 1 for o in rate_list_count]

        for line in lines:
            if line["bits"][bit_i] != rate_list[bit_i]:
                lines_final = [l for l in lines_final if l["number"] != line["number"]]
                if len(lines_final) == 1: break
    
    return int(''.join(str(o) for o in lines_final[0]["bits"]), 2)
    

oxygen_rating = calc_ratings("oxygen")
c02_rating = calc_ratings("c02_rating")

part_2_answer = oxygen_rating * c02_rating
print(part_2_answer)
