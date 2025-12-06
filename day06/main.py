from math import prod

filename = "input.txt"
# Part 1
with open(filename) as f:
    lines = [x.strip() for x in f]

items = [[int(n) for n in x.split()] for x in lines[:-1]] + [lines[-1].split()]
print(sum([sum(t[:-1]) if t[-1] == "+" else prod(t[:-1]) for t in zip(*items)]))

# Part 2
with open(filename) as f:
    lines = [list(x.replace("\n", "").replace(" ", ".")) for x in f]

items = list(map(list, zip(*lines)))

res = 0
coll = []

while len(items) > 0:
    item = items.pop()
    if len("".join(item).strip(".")) > 0:
        coll.append(item)
        op = item[-1]
        if op in ("+", "*"):
            numbers = ["".join(c[:-1]).strip(".") for c in coll]
            numbers = [int(n) for n in numbers if len(n) > 0]

            if op == "+":
                res += sum(numbers)
            else:
                res += prod(numbers)
            coll = []
print(res)
