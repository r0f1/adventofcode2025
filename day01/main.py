with open("input.txt") as f:
    lines = [(x[0], int(x[1:])) for x in f]

pos = 50
part_1 = 0
part_2 = 0
for d, n in lines:
    clicks = n // 100
    rotation = n % 100

    part_2 += clicks

    if d == "R":
        if pos + rotation >= 100:
            part_2 += 1
        pos = (pos + rotation) % 100
    else:
        if pos != 0 and pos - rotation <= 0:
            part_2 += 1
        pos = (pos - rotation) % 100

    if pos == 0:
        part_1 += 1

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
