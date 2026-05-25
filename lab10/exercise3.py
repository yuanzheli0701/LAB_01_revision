import random


def count_cross_edges(groupA, groupB, graph):
    setB = set(groupB)
    count = 0
    for u in groupA:
        for v in graph.get(u, []):
            if v in setB:
                count += 1
    return count


def find_balanced_partition_greedy(graph):
    nodes = list(graph.keys())
    n = len(nodes)
    if n == 0:
        return 0, [], []
    min_size = max(1, int(0.4 * n))

    shuffled = nodes[:]
    random.shuffle(shuffled)
    groupA = set(shuffled[:n // 2])
    groupB = set(shuffled[n // 2:])

    improved = True
    while improved:
        improved = False
        for u in list(groupA) + list(groupB):
            in_A = u in groupA
            source = groupA if in_A else groupB
            target = groupB if in_A else groupA

            if len(source) - 1 < min_size or len(target) + 1 > n - min_size:
                continue

            current_cut = count_cross_edges(list(groupA), list(groupB), graph)
            source.remove(u)
            target.add(u)
            new_cut = count_cross_edges(list(groupA), list(groupB), graph)

            if new_cut < current_cut:
                improved = True
            else:
                target.remove(u)
                source.add(u)

    return count_cross_edges(list(groupA), list(groupB), graph), list(groupA), list(groupB)


def find_balanced_partition_local_search(graph, iterations=10):
    best_cut = float('inf')
    best_A, best_B = None, None

    for _ in range(iterations):
        cut, gA, gB = find_balanced_partition_greedy(graph)
        if cut < best_cut:
            best_cut = cut
            best_A, best_B = gA, gB

    return best_cut, best_A, best_B


def run_tests():
    test_cases = []

    # Test 1: Empty graph
    g1 = {0: [], 1: [], 2: [], 3: [], 4: []}
    test_cases.append(("Empty Graph (5 nodes)", g1))

    # Test 2: Complete graph K4
    g2 = {
        0: [1, 2, 3],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [0, 1, 2]
    }
    test_cases.append(("Complete Graph K4", g2))

    # Test 3: Dumbbell graph (two cliques of 3, linked by 1 edge)
    g3 = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2, 4, 5],
        4: [3, 5],
        5: [3, 4]
    }
    test_cases.append(("Dumbbell Graph (6 nodes)", g3))

    # Test 4: Path graph
    g4 = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3]}
    test_cases.append(("Path Graph (5 nodes)", g4))

    # Test 5: Single node
    g5 = {0: []}
    test_cases.append(("Single Node", g5))

    # Test 6: Two disconnected cliques of 4
    g6 = {
        0: [1, 2, 3],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [0, 1, 2],
        4: [5, 6, 7],
        5: [4, 6, 7],
        6: [4, 5, 7],
        7: [4, 5, 6]
    }
    test_cases.append(("Two Disconnected Cliques K4+K4", g6))

    # Test 7: Star graph
    g7 = {0: [1, 2, 3, 4, 5], 1: [0], 2: [0], 3: [0], 4: [0], 5: [0]}
    test_cases.append(("Star Graph (6 nodes)", g7))

    # Test 8: Cycle graph C6
    g8 = {
        0: [1, 5], 1: [0, 2], 2: [1, 3],
        3: [2, 4], 4: [3, 5], 5: [4, 0]
    }
    test_cases.append(("Cycle Graph C6", g8))

    results = []
    for name, graph in test_cases:
        n = len(graph)
        total_edges = sum(len(v) for v in graph.values()) // 2
        random.seed(42)
        cut, gA, gB = find_balanced_partition_local_search(graph, iterations=20)
        balance_ok = (
            len(gA) >= int(0.4 * n) and len(gB) >= int(0.4 * n)
            if n > 1 else True
        )
        results.append({
            "name": name,
            "nodes": n,
            "edges": total_edges,
            "groupA_size": len(gA) if gA else 0,
            "groupB_size": len(gB) if gB else 0,
            "cross_edges": cut,
            "balanced": balance_ok
        })

    return results


if __name__ == "__main__":
    results = run_tests()
    print(f"{'Test Case':<35} {'N':>4} {'E':>4} {'|A|':>5} {'|B|':>5} {'Cross':>7} {'Balanced':>9}")
    print("-" * 75)
    for r in results:
        print(
            f"{r['name']:<35} {r['nodes']:>4} {r['edges']:>4} "
            f"{r['groupA_size']:>5} {r['groupB_size']:>5} "
            f"{r['cross_edges']:>7} {str(r['balanced']):>9}"
        )