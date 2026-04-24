```python
import random

def split_region(x, y, width, height, min_size):
    if width < min_size or height < min_size:
        return
    half_w = width / 2
    half_h = height / 2
    split_region(x, y, half_w, half_h, min_size)
    split_region(x + half_w, y, half_w, half_h, min_size)
    split_region(x, y + half_h, half_w, half_h, min_size)
    split_region(x + half_w, y + half_h, half_w, half_h, min_size)


def count_points_in_region(points, region):
    rx, ry, rw, rh = region
    count = 0
    for px, py in points:
        if rx <= px < rx + rw and ry <= py < ry + rh:
            count += 1
    return count


def find_dense_regions(points, x, y, width, height, min_size, density_threshold):
    density = count_points_in_region(points, (x, y, width, height)) / (width * height)
    if density <= density_threshold:
        return []
    if width < min_size or height < min_size:
        return [(x, y, width, height)]
    half_w = width / 2
    half_h = height / 2
    return (
        find_dense_regions(points, x, y, half_w, half_h, min_size, density_threshold) +
        find_dense_regions(points, x + half_w, y, half_w, half_h, min_size, density_threshold) +
        find_dense_regions(points, x, y + half_h, half_w, half_h, min_size, density_threshold) +
        find_dense_regions(points, x + half_w, y + half_h, half_w, half_h, min_size, density_threshold)
    )


if __name__ == "__main__":
    points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(200)]

    print("Test 1 - Region at min_size:")
    split_region(0, 0, 10, 10, min_size=10)
    print("  No split (as expected)")

    print("Test 2 - Region smaller than min_size:")
    split_region(0, 0, 5, 10, min_size=10)
    print("  No split (as expected)")

    print("Test 3 - Empty point list:")
    print(" ", count_points_in_region([], (0, 0, 100, 100)))

    print("Test 4 - Points on boundary:")
    boundary_pts = [(0,0),(99,99),(0,99),(99,0)]
    print(" ", count_points_in_region(boundary_pts, (0, 0, 100, 100)))

    print("Test 5 - All points in one corner:")
    corner_pts = [(1, 1)] * 100
    result = find_dense_regions(corner_pts, 0, 0, 100, 100, min_size=10, density_threshold=0.01)
    print(f"  Dense regions found: {len(result)}")

    print("Test 6 - Density below threshold:")
    sparse_pts = [(50, 50)]
    result = find_dense_regions(sparse_pts, 0, 0, 100, 100, min_size=10, density_threshold=0.1)
    print(f"  Dense regions found: {len(result)} (expected 0)")

    print("Test 7 - Entire space dense:")
    dense_pts = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(10000)]
    result = find_dense_regions(dense_pts, 0, 0, 100, 100, min_size=10, density_threshold=0.1)
    print(f"  Dense regions found: {len(result)}")

    print("Test 8 - 1x1 region:")
    split_region(0, 0, 1, 1, min_size=2)
    print("  No infinite recursion (as expected)")
```
