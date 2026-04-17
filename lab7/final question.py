import random
import math

def generate_terrain(width, height, roughness, depth):
    grid = [[0.0] * width for _ in range(height)]
    grid[0][0] = 0
    grid[0][width-1] = 0
    grid[height-1][0] = 0
    grid[height-1][width-1] = 0
    diamond_square(grid, 0, 0, width-1, height-1, roughness, depth)
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
            diff_h = abs(terrain_grid[i][j] - terrain_grid[i][j+1])
            diff_v = abs(terrain_grid[i][j] - terrain_grid[i+1][j])
            if diff_h > threshold or diff_v > threshold:
                suspicious.append((i, j))
    return suspicious

def count_nonempty_boxes(terrain, box_size):
    count = 0
    rows = len(terrain)
    cols = len(terrain[0])
    for i in range(0, rows, box_size):
        for j in range(0, cols, box_size):
            box = [terrain[r][c] for r in range(i, min(i+box_size, rows))
                                  for c in range(j, min(j+box_size, cols))]
            if any(v != 0 for v in box):
                count += 1
    return count

def measure_fractal_dimension(terrain):
    box_sizes = [2, 4, 8, 16, 32]
    counts = []
    for size in box_sizes:
        counts.append(count_nonempty_boxes(terrain, size))
    log_sizes = [math.log(1/s) for s in box_sizes]
    log_counts = [math.log(c) if c > 0 else 0 for c in counts]
    n = len(box_sizes)
    mean_x = sum(log_sizes) / n
    mean_y = sum(log_counts) / n
    slope = sum((log_sizes[i] - mean_x) * (log_counts[i] - mean_y) for i in range(n)) / \
            sum((log_sizes[i] - mean_x) ** 2 for i in range(n))
    return round(slope, 3)

def extract_points(terrain):
    points = []
    for i, row in enumerate(terrain):
        for j, val in enumerate(row):
            if val > 0:
                points.append((i, j))
    return points

def split_region(points, x, y, width, height, min_size, density_threshold):
    if width < min_size or height < min_size:
        return []
    in_region = [(px, py) for (px, py) in points if x <= px < x+width and y <= py < y+height]
    area = width * height
    density = len(in_region) / area if area > 0 else 0
    if density < density_threshold:
        return []
    hw = width // 2
    hh = height // 2
    result = [(x, y, width, height)]
    result += split_region(in_region, x,    y,    hw, hh, min_size, density_threshold)
    result += split_region(in_region, x+hw, y,    hw, hh, min_size, density_threshold)
    result += split_region(in_region, x,    y+hh, hw, hh, min_size, density_threshold)
    result += split_region(in_region, x+hw, y+hh, hw, hh, min_size, density_threshold)
    return result

def generate_and_analyze(width, height, roughness, depth, threshold, min_size, density_threshold):
    terrain = generate_terrain(width, height, roughness, depth)
    dimension = measure_fractal_dimension(terrain)
    warning = dimension < 1.8 or dimension > 2.5
    points = extract_points(terrain)
    regions = split_region(points, 0, 0, width, height, min_size, density_threshold)
    artifacts = detect_artifacts(terrain, threshold)
    return terrain, dimension, warning, regions, artifacts


random.seed(42)

test_cases = [
    (9, 9, 1.0, 3, 0.5, 3, 0.01),
    (9, 9, 0.0, 3, 0.5, 3, 0.01),
    (9, 9, 2.0, 3, 0.5, 3, 0.01),
    (9, 9, 1.0, 3, 0.1, 3, 0.01),
]

print(f"{'Width':<6} {'Height':<7} {'Rough':<6} {'Depth':<6} {'Thresh':<8} {'Dim':<8} {'Warning':<8} {'Regions':<8} {'Artifacts'}")
print("-" * 75)
for (w, h, r, d, t, ms, dt) in test_cases:
    _, dim, warn, regions, artifacts = generate_and_analyze(w, h, r, d, t, ms, dt)
    print(f"{w:<6} {h:<7} {r:<6} {d:<6} {t:<8} {dim:<8} {str(warn):<8} {len(regions):<8} {len(artifacts)}")