with open("input.txt") as f:
    lines_intervals, lines_ids = f.read().split("\n\n")

intervals = [[int(i) for i in x.split("-")] for x in lines_intervals.split()]
ids = [int(i) for i in lines_ids.split()]

# Part 1
result = 0
for id in ids:
    for lb, ub in intervals:
        if lb <= id <= ub:
            result += 1
            break
print(result)

# Part 2

count = 0
n = 0
for lb, ub in sorted(intervals):
    new_n = max(n, ub)
    if lb <= n:
        count += new_n - n
    else:
        count += ub - lb + 1
    n = new_n

print(count)
