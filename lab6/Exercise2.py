class SocialNetwork:
    def __init__(self, users):
        self.all_users = users
        self.adj_list = {user: [] for user in users}

    def add_friendship(self, u1, u2):
        self.adj_list[u1].append(u2)
        self.adj_list[u2].append(u1)

    def dfs_recursive_helper(self, current, visited, order):
        visited.add(current)
        order.append(current)
        for neighbor in self.adj_list[current]:
            if neighbor not in visited:
                self.dfs_recursive_helper(neighbor, visited, order)

    def dfs_recursive(self, start_user):
        visited = set()
        order = []
        self.dfs_recursive_helper(start_user, visited, order)
        return order

    def dfs_iterative(self, start_user):
        visited = set()
        order = []
        stack = [start_user]
        while stack:
            user = stack.pop()
            if user not in visited:
                visited.add(user)
                order.append(user)
                for neighbor in reversed(self.adj_list[user]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

    def find_connected_components(self):
        visited = set()
        components = []
        for user in self.all_users:
            if user not in visited:
                component = self.dfs_recursive(user)
                visited.update(component)
                components.append(component)
        return components

    def is_connected(self):
        if not self.all_users: return True
        return len(self.find_connected_components()) == 1

    def has_path(self, start_user, target_user):
        return target_user in self.dfs_recursive(start_user)

    def find_path(self, start_user, target_user):
        stack = [(start_user, [start_user])]
        visited = {start_user}
        while stack:
            (user, path) = stack.pop()
            if user == target_user:
                return path
            for neighbor in self.adj_list[user]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append((neighbor, path + [neighbor]))
        return None

    def get_connected_components_sizes(self):
        return [len(c) for c in self.find_connected_components()]

    def find_largest_component(self):
        components = self.find_connected_components()
        return max(components, key=len) if components else []

    def find_isolated_users(self):
        return [u for u in self.all_users if len(self.adj_list[u]) == 0]

if __name__ == "__main__":
    network = SocialNetwork(["Alice", "Bob", "Charlie", "David", "Eve", "Frank"])
    network.add_friendship("Alice", "Bob")
    network.add_friendship("Bob", "Charlie")
    network.add_friendship("David", "Eve")

    print("DFS Recursive (Alice):", network.dfs_recursive("Alice"))
    print("DFS Iterative (Alice):", network.dfs_iterative("Alice"))
    print("Connected Components:", network.find_connected_components())
    print("Is Connected:", network.is_connected())
    print("Path Alice -> Charlie:", network.find_path("Alice", "Charlie"))
    print("Path Alice -> David:", network.find_path("Alice", "David"))
    print("Component Sizes:", network.get_connected_components_sizes())
    print("Largest Component:", network.find_largest_component())
    print("Isolated Users:", network.find_isolated_users())