def is_within_budget(selection, costs, budget):
    total_cost = sum(costs[i] for i in selection)
    return total_cost <= budget


def maximize_reach(budget, costs, influences):
    """
    Exact solution for 0/1 Knapsack.
    Returns: (max_influence, selected_users_list)
    Complexity: O(N * budget)
    """
    n = len(costs)

    dp = [0] * (budget + 1)
    keep = [[False] * (budget + 1) for _ in range(n)]

    for i in range(n):
        cost = costs[i]
        influence = influences[i]

        for b in range(budget, cost - 1, -1):
            if dp[b - cost] + influence > dp[b]:
                dp[b] = dp[b - cost] + influence
                keep[i][b] = True

    selected = []
    b = budget

    for i in range(n - 1, -1, -1):
        if keep[i][b]:
            selected.append(i)
            b -= costs[i]

    selected.reverse()
    return dp[budget], selected


def fast_alternative_strategy(budget, costs, influences):
    """
    Greedy strategy by influence / cost ratio.
    This is fast but not always optimal.
    Returns: (total_influence, selected_users_list)
    """
    n = len(costs)

    users = list(range(n))
    users.sort(
        key=lambda i: influences[i] / costs[i] if costs[i] != 0 else float("inf"),
        reverse=True
    )

    selected = []
    total_cost = 0
    total_influence = 0

    for i in users:
        if total_cost + costs[i] <= budget:
            selected.append(i)
            total_cost += costs[i]
            total_influence += influences[i]

    return total_influence, selected


def decision_knapsack(budget, costs, influences, target_influence):
    """
    Final Questions: Decision version.
    Question: Does there exist a subset with total cost <= budget
    and total influence >= target_influence?
    """
    max_influence, selected = maximize_reach(budget, costs, influences)

    if max_influence >= target_influence:
        return True, selected

    return False, []


def classify_lab9_problems():
    """
    Final Questions: Classification of the three Lab9 problems.
    """
    return {
        "Exercise 1 - Minimum Dominating Set": "NP-Hard optimization; decision version is NP-Complete",
        "Exercise 2 - Graph Coloring": "NP-Hard optimization; k-coloring decision version is NP-Complete",
        "Exercise 3 - 0/1 Knapsack": "NP-Hard optimization; decision version is NP-Complete; pseudo-polynomial DP exists"
    }


def run_edge_case_tests():
    print("=== Exercise 3: Normal Case ===")
    budget = 10
    costs = [6, 3, 4, 2]
    influences = [30, 14, 16, 9]

    exact_value, exact_selected = maximize_reach(budget, costs, influences)
    greedy_value, greedy_selected = fast_alternative_strategy(budget, costs, influences)

    print("Exact:", exact_value, exact_selected)
    print("Greedy:", greedy_value, greedy_selected)
    print("Exact within budget:", is_within_budget(exact_selected, costs, budget))
    print("Greedy within budget:", is_within_budget(greedy_selected, costs, budget))

    print("\n=== Budget = 0 ===")
    budget = 0
    costs = [1, 2, 3]
    influences = [10, 20, 30]
    print(maximize_reach(budget, costs, influences))

    print("\n=== Empty Input ===")
    budget = 10
    costs = []
    influences = []
    print(maximize_reach(budget, costs, influences))

    print("\n=== Greedy Counterexample ===")
    budget = 50
    costs = [10, 20, 30]
    influences = [60, 100, 120]

    exact_value, exact_selected = maximize_reach(budget, costs, influences)
    greedy_value, greedy_selected = fast_alternative_strategy(budget, costs, influences)

    print("Exact:", exact_value, exact_selected)
    print("Greedy:", greedy_value, greedy_selected)

    print("\n=== Decision Version ===")
    budget = 50
    costs = [10, 20, 30]
    influences = [60, 100, 120]
    target = 220

    exists, selected = decision_knapsack(budget, costs, influences, target)
    print("Target influence:", target)
    print("Exists:", exists)
    print("Selected:", selected)

    print("\n=== Classification ===")
    classifications = classify_lab9_problems()
    for problem, result in classifications.items():
        print(problem + ":", result)


if __name__ == "__main__":
    run_edge_case_tests()
