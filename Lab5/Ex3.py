from collections import deque

class GeneralizedCategoryNode:
    def __init__(self, category_id, name, post_count):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


class BinaryNode:
    def __init__(self, category_id, name, post_count):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.left = None
        self.right = None


def binary_to_generalized(binary_root):
    if binary_root is None:
        return None

    gen_node = GeneralizedCategoryNode(
        binary_root.category_id, binary_root.name, binary_root.post_count
    )

    if binary_root.left:
        gen_node.add_child(binary_to_generalized(binary_root.left))
    if binary_root.right:
        gen_node.add_child(binary_to_generalized(binary_root.right))

    return gen_node


def generalized_to_binary(gen_root):
    if gen_root is None:
        return None

    bin_node = BinaryNode(gen_root.category_id, gen_root.name, gen_root.post_count)

    if gen_root.children:
        bin_node.left = generalized_to_binary(gen_root.children[0])
        cur = bin_node.left
        for sibling in gen_root.children[1:]:
            cur.right = generalized_to_binary(sibling)
            cur = cur.right

    return bin_node


def pre_order_generalized(node):
    if node is None:
        return []
    result = [node.name]
    for child in node.children:
        result.extend(pre_order_generalized(child))
    return result


def post_order_generalized(node):
    if node is None:
        return []
    result = []
    for child in node.children:
        result.extend(post_order_generalized(child))
    result.append(node.name)
    return result


def level_order_generalized(node):
    if node is None:
        return []
    result = []
    queue = deque([node])
    while queue:
        cur = queue.popleft()
        result.append(cur.name)
        for child in cur.children:
            queue.append(child)
    return result


def calculate_fan_out(node):
    if node is None:
        return 0
    max_children = len(node.children)
    for child in node.children:
        max_children = max(max_children, calculate_fan_out(child))
    return max_children


def calculate_height_generalized(node):
    if node is None:
        return -1
    if not node.children:
        return 0
    return 1 + max(calculate_height_generalized(c) for c in node.children)


def count_nodes_generalized(node):
    if node is None:
        return 0
    return 1 + sum(count_nodes_generalized(c) for c in node.children)


def count_leaves_generalized(node):
    if node is None:
        return 0
    if not node.children:
        return 1
    return sum(count_leaves_generalized(c) for c in node.children)


def calculate_branching_factor(node):
    total_children = [0]
    non_leaf_count = [0]

    def dfs(n):
        if not n.children:
            return
        non_leaf_count[0] += 1
        total_children[0] += len(n.children)
        for child in n.children:
            dfs(child)

    dfs(node)
    if non_leaf_count[0] == 0:
        return 0.0
    return total_children[0] / non_leaf_count[0]
