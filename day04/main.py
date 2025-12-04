import numpy as np
from scipy.ndimage import convolve

with open("input.txt") as f:
    lines = [[int(c == "@") for c in x.strip()] for x in f]

kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
arr = np.array(lines)

result = 0
i = 0

while True:
    locations = convolve(arr, kernel, mode="constant")
    locations = np.logical_and(arr, locations < 4).astype(int)
    n_removed = np.sum(locations)
    if i == 0:
        print(n_removed)
    if n_removed == 0:
        break
    result += n_removed
    arr = arr - locations
    i += 1

print(result)
