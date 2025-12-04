from operator import itemgetter


def get_best_idx(digits, bounds, selected):
    while True:
        lb, ub = bounds[-1]

        dig = [(i, d) for i, d in enumerate(digits) if not selected[i] and i >= lb and i < ub]

        if len(dig) == 0:
            bounds.pop()
            return get_best_idx(digits, bounds, selected)
        break

    idx, _ = max(dig, key=itemgetter(1))
    selected[idx] = 1
    return idx


with open("input.txt") as f:
    lines = [x.strip() for x in f]


for limit in [2, 12]:
    results = []

    for line in lines:
        digits = [int(c) for c in line]
        selected = [0] * len(digits)

        bounds = [(0, len(digits))]
        prev_lb = 0
        prev_ub = len(digits)

        prev_idx = -1
        while sum(selected) < limit:
            idx = get_best_idx(digits, bounds, selected)

            if idx > prev_idx:
                lb, ub = idx + 1, prev_ub
            else:
                lb, ub = prev_lb, idx - 1

            bounds.append((lb, ub))
            prev_lb, prev_ub = lb, ub

        result = "".join(str(d) for s, d in zip(selected, digits) if s)
        results.append(int(result))

    print(sum(results))
