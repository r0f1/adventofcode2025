from collections import defaultdict

with open("input.txt") as f:
    lines = [x.strip() for x in f]

active = {(lines[0].index("S")): 1}

n_splits = 0
for line in lines[1:]:
    curr = defaultdict(int)
    for x, n in active.items():
        if line[x] == "^":
            n_splits += 1
            curr[x - 1] += n
            curr[x + 1] += n
        else:
            curr[x] += n
    active = curr

print(n_splits)
print(sum(active.values()))
