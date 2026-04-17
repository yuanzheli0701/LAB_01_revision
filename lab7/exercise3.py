import random
import math


def midpoint_displacement(x1, y1, x2, y2, roughness, depth):
    if depth == 0:
        return [(x1, y1), (x2, y2)]

    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2 + roughness * random.uniform(-1, 1)

    left = midpoint_displacement(x1, y1, mx, my, roughness * 0.5, depth - 1)
    right = midpoint_displacement(mx, my, x2, y2, roughness * 0.5, depth - 1)

    return left + right[1:]


def generate_terrain(width, height, roughness, depth):
    grid = [[0.0] * width for _ in range(height)]

    grid[0][0] = 0
    grid[0][width - 1] = 0
    grid[height - 1][0] = 0
    grid[height - 1][width - 1] = 0

    diamond_square(grid, 0, 0, width - 1, height - 1, roughness, depth)
    return grid


def diamond_square(grid, x1, y1, x2, y2, roughness, depth):
    if depth == 0 or (x2 - x1) < 2:
        return

    mx = (x1 + x2) // 2
    my = (y1 + y2) // 2

    grid[my][mx] = (grid[y1][x1] + grid[y1][x2] +
                    grid[y2][x1] + grid[y2][x2]) / 4 + roughness * random.uniform(-1, 1)

    grid[y1][mx] = (grid[y1][x1] + grid[y1][x2] + grid[my][mx]) / 3 + roughness * random.uniform(-1, 1)
    grid[y2][mx] = (grid[y2][x1] + grid[y2][x2] + grid[my][mx]) / 3 + roughness * random.uniform(-1, 1)
    grid[my][x1] = (grid[y1][x1] + grid[y2][x1] + grid[my][mx]) / 3 + roughness * random.uniform(-1, 1)
    grid[my][x2] = (grid[y1][x2] + grid[y2][x2] + grid[my][mx]) / 3 + roughness * random.uniform(-1, 1)

    diamond_square(grid, x1, y1, mx, my, roughness * 0.5, depth - 1)
    diamond_square(grid, mx, y1, x2, my, roughness * 0.5, depth - 1)
    diamond_square(grid, x1, my, mx, y2, roughness * 0.5, depth - 1)
    diamond_square(grid, mx, my, x2, y2, roughness * 0.5, depth - 1)


def detect_artifacts(terrain_grid, threshold):
    suspicious = []
    rows = len(terrain_grid)
    cols = len(terrain_grid[0])

    for i in range(rows - 1):
        for j in range(cols - 1):
            diff_h = abs(terrain_grid[i][j] - terrain_grid[i][j + 1])
            diff_v = abs(terrain_grid[i][j] - terrain_grid[i + 1][j])
            if diff_h > threshold or diff_v > threshold:
                suspicious.append((i, j))

    return suspicious


random.seed(42)

print("=== midpoint_displacement ===")
tests_md = [
    (0, 0, 8, 0, 1.0, 3),
    (0, 0, 4, 0, 0.0, 2),
    (0, 0, 4, 0, 2.0, 2),
    (0, 0, 2, 0, 1.0, 0),
]
for (x1, y1, x2, y2, r, d) in tests_md:
    result = midpoint_displacement(x1, y1, x2, y2, r, d)
    print(f"  ({x1},{y1})->({x2},{y2}) r={r} d={d} => {len(result)} points, first={result[0]}, last={result[-1]}")

print()
print("=== generate_terrain + detect_artifacts ===")
tests_terrain = [
    (5, 5, 1.0, 2, 0.5),
    (5, 5, 0.0, 2, 0.5),
    (5, 5, 2.0, 2, 0.5),
    (3, 3, 1.0, 1, 0.3),
]
for (w, h, r, d, thresh) in tests_terrain:
    grid = generate_terrain(w, h, r, d)
    artifacts = detect_artifacts(grid, thresh)
    center = round(grid[h // 2][w // 2], 3)
    print(f"  w={w} h={h} r={r} d={d} thresh={thresh} => center={center}, artifacts={len(artifacts)}")