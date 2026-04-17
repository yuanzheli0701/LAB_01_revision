from collections import deque

class SocialEngine:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def suggest_friends(self, u):
        friends = set(self.adj[u])
        suggestions = {}
        for f in friends:
            for fof in self.adj[f]:
                if fof != u and fof not in friends:
                    suggestions[fof] = suggestions.get(fof, 0) + 1
        
        sorted_sugs = sorted(suggestions.keys(), key=lambda k: suggestions[k], reverse=True)
        return sorted_sugs[:10] 

    def shortest_path(self, start, target):
        queue = deque([[start]])
        visited = {start}
        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == target:
                return path
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        return []

    def find_isolated(self):
        return [i for i in range(self.n) if len(self.adj[i]) == 0]

    def get_connected_components(self):
        visited = set()
        components = []
        for i in range(self.n):
            if i not in visited:
                comp = []
                stack = [i]
                visited.add(i)
                while stack:
                    node = stack.pop()
                    comp.append(node)
                    for neighbor in self.adj[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
                components.append(comp)
        return components

    def distance_distribution(self, start):
        queue = deque([(start, 0)])
        visited = {start}
        dist_map = {}
        while queue:
            node, dist = queue.popleft()
            dist_map[dist] = dist_map.get(dist, 0) + 1
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return dist_map
