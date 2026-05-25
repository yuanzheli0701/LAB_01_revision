def normalize_graph(graph):
    """
    Supports:
    1. Adjacency list as dict: {0: [1, 2], 1: [0], ...}
    2. Adjacency list as list: [[1, 2], [0], ...]
    3. Adjacency matrix: [[0, 1], [1, 0]]
    Returns: dict[node] = set(neighbors)
    """
    if isinstance(graph, dict):
        normalized = {node: set(neighbors) for node, neighbors in graph.items()}
        for node, neighbors in list(normalized.items()):
            for neighbor in neighbors:
                normalized.setdefault(neighbor, set()).add(node)
        return normalized

    n = len(graph)

    is_matrix = all(
        isinstance(row, list)
        and len(row) == n
        and all(value in (0, 1, True, False) for value in row)
        for row in graph
    )

    if is_matrix:
        normalized = {i: set() for i in range(n)}
        for i in range(n):
            for j in range(n):
                if graph[i][j]:
                    normalized[i].add(j)
                    normalized[j].add(i)
        return normalized

    normalized = {i: set(graph[i]) for i in range(n)}
    for node, neighbors in list(normalized.items()):
        for neighbor in neighbors:
            normalized.setdefault(neighbor, set()).add(node)

    return normalized


def is_valid_invitation(invited, graph):
    """
    Returns True if no two invited users have a conflict edge.
    """
    graph = normalize_graph(graph)
    invited_set = set(invited)

    for user in invited_set:
        for neighbor in graph.get(user, set()):
            if neighbor in invited_set:
                return False

    return True


def find_max_invitations_exact(graph):
    """
    Exact Maximum Independent Set using backtracking with pruning.

    Pruning rule:
    if len(current) + len(remaining) <= len(best), stop searching.
    """
    graph = normalize_graph(graph)
    nodes = list(graph.keys())

    best = []

    def backtrack(current, remaining):
        nonlocal best

        if len(current) + len(remaining) <= len(best):
            return

        if not remaining:
            if len(current) > len(best):
                best = current[:]
            return

        node = remaining[0]

        # Option 1: include node
        new_remaining = [
            other for other in remaining[1:]
            if other not in graph[node]
        ]
        backtrack(current + [node], new_remaining)

        # Option 2: exclude node
        backtrack(current, remaining[1:])

    # A useful ordering: try low-degree nodes first
    nodes.sort(key=lambda node: len(graph[node]))

    backtrack([], nodes)

    return len(best), best


def find_max_invitations_greedy(graph):
    """
    Greedy heuristic:
    repeatedly choose the node with smallest degree,
    add it to invitation list,
    remove it and its neighbors.
    """
    graph = normalize_graph(graph)

    remaining = set(graph.keys())
    invited = []

    while remaining:
        node = min(
            remaining,
            key=lambda user: len(graph[user] & remaining)
        )

        invited.append(node)

        remaining.remove(node)
        remaining -= graph[node]

    return len(invited), invited


# Example usage
if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2],
        4: []
    }

    invited = [0, 3, 4]
    print("Valid invitation:", is_valid_invitation(invited, graph))

    exact_size, exact_invited = find_max_invitations_exact(graph)
    print("Exact solution:", exact_size, exact_invited)

    greedy_size, greedy_invited = find_max_invitations_greedy(graph)
    print("Greedy solution:", greedy_size, greedy_invited)
