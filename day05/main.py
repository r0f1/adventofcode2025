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
sorted_intervals = sorted(intervals)

count = 0
n = 0
while len(sorted_intervals) > 0:
    curr_lb, curr_ub = sorted_intervals.pop(0)
    new_n = max(n, curr_ub)
    if curr_lb <= n:
        count += new_n - n
    else:
        count += curr_ub - curr_lb + 1
    n = new_n

print(count)
