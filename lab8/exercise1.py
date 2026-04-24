class Node:
    def __init__(self, user_id, name, friends):
        self.user_id = user_id
        self.name = name
        self.friends = friends
        self.left = None
        self.right = None


class UserBST:
    def __init__(self):
        self.root = None

    def insert(self, user_id, name, friends_list):
        self.root = self._insert_rec(self.root, user_id, name, friends_list)

    def _insert_rec(self, node, user_id, name, friends_list):
        if node is None:
            return Node(user_id, name, friends_list)
        if user_id < node.user_id:
            node.left = self._insert_rec(node.left, user_id, name, friends_list)
        elif user_id > node.user_id:
            node.right = self._insert_rec(node.right, user_id, name, friends_list)
        return node

    def find(self, user_id):
        return self._find_rec(self.root, user_id)

    def _find_rec(self, node, user_id):
        if node is None:
            return None
        if user_id == node.user_id:
            return node
        elif user_id < node.user_id:
            return self._find_rec(node.left, user_id)
        else:
            return self._find_rec(node.right, user_id)

    def inorder_traversal(self):
        result = []
        self._inorder_rec(self.root, result)
        return result

    def _inorder_rec(self, node, result):
        if node is None:
            return
        self._inorder_rec(node.left, result)
        result.append(node.user_id)
        self._inorder_rec(node.right, result)

    def delete(self, user_id):
        self.root = self._delete_rec(self.root, user_id)

    def _delete_rec(self, node, user_id):
        if node is None:
            return None
        if user_id < node.user_id:
            node.left = self._delete_rec(node.left, user_id)
        elif user_id > node.user_id:
            node.right = self._delete_rec(node.right, user_id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            successor = self._find_min(node.right)
            node.user_id = successor.user_id
            node.name = successor.name
            node.friends = successor.friends
            node.right = self._delete_rec(node.right, successor.user_id)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def suggest_friends(self, user_id, max_suggestions=5):
        user = self.find(user_id)
        if user is None:
            return []
        direct_friends = set(user.friends)
        frequency = {}
        for friend_id in user.friends:
            friend_node = self.find(friend_id)
            if friend_node is None:
                continue
            for fof_id in friend_node.friends:
                if fof_id != user_id and fof_id not in direct_friends:
                    frequency[fof_id] = frequency.get(fof_id, 0) + 1
        candidates = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        return [uid for uid, _ in candidates[:max_suggestions]]

    def get_height(self):
        return self._height_rec(self.root)

    def _height_rec(self, node):
        if node is None:
            return 0
        return 1 + max(self._height_rec(node.left), self._height_rec(node.right))

    def is_balanced(self):
        return self._check_balanced(self.root) != -1

    def _check_balanced(self, node):
        if node is None:
            return 0
        left_h = self._check_balanced(node.left)
        if left_h == -1:
            return -1
        right_h = self._check_balanced(node.right)
        if right_h == -1:
            return -1
        if abs(left_h - right_h) > 1:
            return -1
        return 1 + max(left_h, right_h)

    def get_leaf_count(self):
        return self._count_leaves(self.root)

    def _count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaves(node.left) + self._count_leaves(node.right)


if __name__ == "__main__":
    bst = UserBST()

    bst.insert(10, "alice",   [20, 30])
    bst.insert(20, "bob",     [10, 30, 40])
    bst.insert(30, "charlie", [10, 20, 50])
    bst.insert(40, "diana",   [20, 50])
    bst.insert(50, "eve",     [30, 40])
    bst.insert(5,  "frank",   [10])

    print("= insert + inorder_traversal =")
    print(bst.inorder_traversal())

    print("\n= find (existing) =")
    node = bst.find(20)
    print(node.name if node else None)

    print("\n= find (non-existing) =")
    print(bst.find(99))

    print("\n= get_height =")
    print(bst.get_height())

    print("\n= is_balanced =")
    print(bst.is_balanced())

    print("\n= get_leaf_count =")
    print(bst.get_leaf_count())

    print("\n= suggest_friends (user 10) =")
    print(bst.suggest_friends(10))

    print("\n= suggest_friends (non-existing user) =")
    print(bst.suggest_friends(99))

    print("\n= delete leaf node (5) =")
    bst.delete(5)
    print(bst.inorder_traversal())

    print("\n= delete node with one child (40) =")
    bst.delete(40)
    print(bst.inorder_traversal())

    print("\n= delete node with two children (20) =")
    bst.delete(20)
    print(bst.inorder_traversal())

    print("\n= delete non-existing node (99) =")
    bst.delete(99)
    print(bst.inorder_traversal())

    print("\n=empty tree edge cases =")
    empty = UserBST()
    print(empty.find(1))
    print(empty.inorder_traversal())
    print(empty.get_height())
    print(empty.is_balanced())
    print(empty.get_leaf_count())
    print(empty.suggest_friends(1))

    print("\n= degenerate tree (sorted insertion) =")
    deg = UserBST()
    for i in [1, 2, 3, 4, 5]:
        deg.insert(i, f"user{i}", [])
      print("height:", deg.get_height())
    print("is_balanced:", deg.is_balanced())

    print("\n= suggest_friends max_suggestions=2 =")
    bst2 = UserBST()
    bst2.insert(1, "a", [2, 3])
    bst2.insert(2, "b", [1, 3, 4, 5])
    bst2.insert(3, "c", [1, 2, 4, 5])
    bst2.insert(4, "d", [2, 3])
    bst2.insert(5, "e", [2, 3])
    print(bst2.suggest_friends(1, max_suggestions=2))