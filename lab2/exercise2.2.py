class SocialNetwork:
    def __init__(self):
        self.users = {}

    def add_user_friends(self, user_id, friends_list):
        self.users[user_id] = set(friends_list)

    def get_mutual_friends(self, user_a, user_b):
        return self.users[user_a].intersection(self.users[user_b])

    def get_unique_friends(self, user_a, user_b):
        return self.users[user_a].difference(self.users[user_b])

    def get_all_unique_friends(self, user_a, user_b):
        return self.users[user_a].union(self.users[user_b])

    def calculate_jaccard_similarity(self, user_a, user_b):
        intersection_size = len(self.get_mutual_friends(user_a, user_b))
        union_size = len(self.get_all_unique_friends(user_a, user_b))

        if union_size == 0:
            return 0.0
        return intersection_size / union_size

    def get_friend_suggestions(self, user_id):
        current_friends = self.users[user_id]
        suggestions = set()

        for friend in current_friends:
            if friend in self.users:
                fof = self.users[friend]
                suggestions.update(fof)

        suggestions.difference_update(current_friends)
        suggestions.discard(user_id)
        return suggestions


network = SocialNetwork()
network.add_user_friends(100, [101, 102, 103, 104, 105])
network.add_user_friends(200, [103, 104, 106, 107, 108])

mutual = network.get_mutual_friends(100, 200)
jaccard = network.calculate_jaccard_similarity(100, 200)

print(f"mutual acquaintance: {mutual}")
print(f"Jaccard similarity: {jaccard:.2f}")
