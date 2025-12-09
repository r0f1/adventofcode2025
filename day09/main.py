from itertools import combinations

import numpy as np
from skimage.segmentation import flood_fill

with open("test.txt") as f:
    points = [[int(i) for i in x.split(",")] for x in f]


def area(a, b):
    return (1 + abs(a[0] - b[0])) * (1 + abs(a[1] - b[1]))


print(max(area(a, b) for a, b in combinations(points, 2)))

arr = np.zeros((15, 15), dtype=np.uint8)
for a, b in zip(points, points[1:] + [points[0]]):
    start_x, start_y = min(a[0], b[0]), min(a[1], b[1])
    end_x, end_y = max(a[0], b[0]), max(a[1], b[1])
    if start_x == end_x:
        for y in range(start_y, end_y + 1):
            arr[(y, start_x)] = 1
    else:
        for x in range(start_x, end_x + 1):
            arr[(start_y, x)] = 1

arr = flood_fill(arr, (0, 0), 2)
arr = (arr < 2).astype(np.uint8)

res = 0
for a, b in combinations(points, 2):
    start_x, start_y = min(a[0], b[0]), min(a[1], b[1])
    end_x, end_y = max(a[0], b[0]), max(a[1], b[1])
    sel = arr[start_y:end_y, start_x:end_x]
    if not np.any(sel == 0):
        res = max(res, area(a, b))
print(res)


# print(len(list(combinations(points, 2))))

# 173741700 too low
