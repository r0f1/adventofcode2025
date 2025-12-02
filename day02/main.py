with open("input.txt") as f:
    intervals = [(int(lb), int(ub)) for lb, ub in [x.split("-") for x in f.read().split(",")]]

part_1 = 0
part_2 = 0

for lb, ub in intervals:
    for n in range(lb, ub + 1):
        s = str(n)

        if len(s) % 2 == 0 and s[len(s) // 2 :] == s[: len(s) // 2]:
            part_1 += n

        for k in range(1, len(s) // 2 + 1):
            n_chunks, remainder = divmod(len(s), k)
            if remainder == 0 and all(s[:k] == s[k * i : k * (i + 1)] for i in range(n_chunks)):
                part_2 += n
                break

print(part_1)
print(part_2)
