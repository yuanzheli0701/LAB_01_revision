class CategoryNode:
    def __init__(self, category_id, name, post_count):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.left = None
        self.right = None
        self.parent = None


def create_node(id, name, post_count):
    return CategoryNode(id, name, post_count)


def calculate_height(node):
    if node is None:
        return -1
    left_h = calculate_height(node.left)
    right_h = calculate_height(node.right)
    return 1 + max(left_h, right_h)


def calculate_node_height(root, target_id):
    node = find_category(root, target_id)
    if node is None:
        return -1
    depth = 0
    current = node
    while current.parent is not None:
        depth = depth + 1
        current = current.parent
    return depth


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


def is_balanced(node):
    if node is None:
        return True
    left_h = calculate_height(node.left)
    right_h = calculate_height(node.right)
    if abs(left_h - right_h) > 1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)


def is_full_binary_tree(node):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return True
    if node.left is not None and node.right is not None:
        return is_full_binary_tree(node.left) and is_full_binary_tree(node.right)
    return False


def is_perfect_binary_tree(node):
    h = calculate_height(node)
    n = count_nodes(node)
    return n == (2 ** (h + 1) - 1)


def is_complete_binary_tree(root):
    if root is None:
        return True
    from collections import deque
    queue = deque()
    found_null = False
    queue.append(root)
    while queue:
        current = queue.popleft()
        if current is None:
            found_null = True
        else:
            if found_null:
                return False
            queue.append(current.left)
            queue.append(current.right)
    return True


def find_category(node, target_id):
    if node is None:
        return None
    if node.category_id == target_id:
        return node
    result = find_category(node.left, target_id)
    if result is not None:
        return result
    return find_category(node.right, target_id)


def find_path_to_root(root, target_id):
    node = find_category(root, target_id)
    if node is None:
        return []
    path = []
    current = node
    while current is not None:
        path.append(current.name)
        current = current.parent
    return path


def lowest_common_ancestor(node, id1, id2):
    if node is None:
        return None
    if node.category_id == id1 or node.category_id == id2:
        return node
    left_lca = lowest_common_ancestor(node.left, id1, id2)
    right_lca = lowest_common_ancestor(node.right, id1, id2)
    if left_lca is not None and right_lca is not None:
        return node
    if left_lca is not None:
        return left_lca
    return right_lca


def build_example_tree():
    tech = create_node("1", "Technology", 150)
    programming = create_node("2", "Programming", 85)
    design = create_node("3", "Design", 65)
    python = create_node("4", "Python", 42)
    java = create_node("5", "Java", 30)
    uiux = create_node("6", "UI/UX", 38)
    graphics = create_node("7", "Graphics", 22)
    django = create_node("8", "Django", 18)
    flask = create_node("9", "Flask", 12)

    tech.left = programming
    tech.right = design
    programming.left = python
    programming.right = java
    design.left = uiux
    design.right = graphics
    python.left = django
    python.right = flask

    programming.parent = tech
    design.parent = tech
    python.parent = programming
    java.parent = programming
    uiux.parent = design
    graphics.parent = design
    django.parent = python
    flask.parent = python

    return tech


def build_empty_tree():
    return None


def build_single_node_tree():
    return create_node("1", "Root", 100)


def build_left_skewed_tree():
    root = create_node("1", "A", 10)
    node2 = create_node("2", "B", 20)
    node3 = create_node("3", "C", 30)
    node4 = create_node("4", "D", 40)
    root.left = node2
    node2.parent = root
    node2.left = node3
    node3.parent = node2
    node3.left = node4
    node4.parent = node3
    return root


def build_right_skewed_tree():
    root = create_node("1", "A", 10)
    node2 = create_node("2", "B", 20)
    node3 = create_node("3", "C", 30)
    node4 = create_node("4", "D", 40)
    root.right = node2
    node2.parent = root
    node2.right = node3
    node3.parent = node2
    node3.right = node4
    node4.parent = node3
    return root


def build_unbalanced_tree():
    root = create_node("1", "A", 10)
    node2 = create_node("2", "B", 20)
    node3 = create_node("3", "C", 30)
    node4 = create_node("4", "D", 40)
    node5 = create_node("5", "E", 50)
    root.left = node2
    node2.parent = root
    root.right = node3
    node3.parent = root
    node2.left = node4
    node4.parent = node2
    node4.left = node5
    node5.parent = node4
    return root


def build_perfect_tree():
    root = create_node("1", "A", 10)
    node2 = create_node("2", "B", 20)
    node3 = create_node("3", "C", 30)
    node4 = create_node("4", "D", 40)
    node5 = create_node("5", "E", 50)
    node6 = create_node("6", "F", 60)
    node7 = create_node("7", "G", 70)
    root.left = node2
    node2.parent = root
    root.right = node3
    node3.parent = root
    node2.left = node4
    node4.parent = node2
    node2.right = node5
    node5.parent = node2
    node3.left = node6
    node6.parent = node3
    node3.right = node7
    node7.parent = node3
    return root


def build_complete_tree():
    root = create_node("1", "A", 10)
    node2 = create_node("2", "B", 20)
    node3 = create_node("3", "C", 30)
    node4 = create_node("4", "D", 40)
    node5 = create_node("5", "E", 50)
    node6 = create_node("6", "F", 60)
    root.left = node2
    node2.parent = root
    root.right = node3
    node3.parent = root
    node2.left = node4
    node4.parent = node2
    node2.right = node5
    node5.parent = node2
    node3.left = node6
    node6.parent = node3
    return root


def build_incomplete_tree():
    root = create_node("1", "A", 10)
    node2 = create_node("2", "B", 20)
    node3 = create_node("3", "C", 30)
    node4 = create_node("4", "D", 40)
    node5 = create_node("5", "E", 50)
    root.left = node2
    node2.parent = root
    root.right = node3
    node3.parent = root
    node2.left = node4
    node4.parent = node2
    node3.right = node5
    node5.parent = node3
    return root


def build_large_tree(depth, counter=[0]):
    if depth < 0:
        return None
    counter[0] += 1
    node = create_node(str(counter[0]), f"Node{counter[0]}", counter[0] * 10)
    node.left = build_large_tree(depth - 1, counter)
    node.right = build_large_tree(depth - 1, counter)
    if node.left:
        node.left.parent = node
    if node.right:
        node.right.parent = node
    return node


def run_tests():
    print("=" * 50)
    print("TEST SUITE")
    print("=" * 50)

    print("\n1. Empty Tree")
    root = build_empty_tree()
    print(f"   calculate_height: {calculate_height(root)}")
    print(f"   count_nodes: {count_nodes(root)}")
    print(f"   count_leaves: {count_leaves(root)}")
    print(f"   is_balanced: {is_balanced(root)}")
    print(f"   is_full_binary_tree: {is_full_binary_tree(root)}")
    print(f"   is_perfect_binary_tree: {is_perfect_binary_tree(root)}")
    print(f"   is_complete_binary_tree: {is_complete_binary_tree(root)}")
    print(f"   find_category: {find_category(root, '1')}")
    print(f"   find_path_to_root: {find_path_to_root(root, '1')}")

    print("\n2. Single Node Tree")
    root = build_single_node_tree()
    print(f"   calculate_height: {calculate_height(root)}")
    print(f"   count_nodes: {count_nodes(root)}")
    print(f"   count_leaves: {count_leaves(root)}")
    print(f"   is_balanced: {is_balanced(root)}")
    print(f"   is_full_binary_tree: {is_full_binary_tree(root)}")
    print(f"   is_perfect_binary_tree: {is_perfect_binary_tree(root)}")
    print(f"   is_complete_binary_tree: {is_complete_binary_tree(root)}")
    print(f"   find_category: {find_category(root, '1').name}")
    print(f"   find_path_to_root: {find_path_to_root(root, '1')}")

    print("\n3. Left Skewed Tree")
    root = build_left_skewed_tree()
    print(f"   calculate_height: {calculate_height(root)}")
    print(f"   count_nodes: {count_nodes(root)}")
    print(f"   count_leaves: {count_leaves(root)}")
    print(f"   is_balanced: {is_balanced(root)}")
    print(f"   is_full_binary_tree: {is_full_binary_tree(root)}")
    print(f"   is_complete_binary_tree: {is_complete_binary_tree(root)}")
    print(f"   calculate_node_height('4'): {calculate_node_height(root, '4')}")

    print("\n4. Right Skewed Tree")
    root = build_right_skewed_tree()
    print(f"   calculate_height: {calculate_height(root)}")
    print(f"   count_nodes: {count_nodes(root)}")
    print(f"   count_leaves: {count_leaves(root)}")
    print(f"   is_balanced: {is_balanced(root)}")
    print(f"   is_full_binary_tree: {is_full_binary_tree(root)}")
    print(f"   is_complete_binary_tree: {is_complete_binary_tree(root)}")

    print("\n5. Unbalanced Tree")
    root = build_unbalanced_tree()
    print(f"   calculate_height: {calculate_height(root)}")
    print(f"   count_nodes: {count_nodes(root)}")
    print(f"   count_leaves: {count_leaves(root)}")
    print(f"   is_balanced: {is_balanced(root)}")
    print(f"   is_full_binary_tree: {is_full_binary_tree(root)}")

    print("\n6. Perfect Binary Tree (height 2)")
    root = build_perfect_tree()
    print(f"   calculate_height: {calculate_height(root)}")
    print(f"   count_nodes: {count_nodes(root)}")
    print(f"   count_leaves: {count_leaves(root)}")
    print(f"   is_balanced: {is_balanced(root)}")
    print(f"   is_full_binary_tree: {is_full_binary_tree(root)}")
    print(f"   is_perfect_binary_tree: {is_perfect_binary_tree(root)}")
    print(f"   is_complete_binary_tree: {is_complete_binary_tree(root)}")
    lca = lowest_common_ancestor(root, "4", "5")
    print(f"   LCA of 4 and 5: {lca.name if lca else None}")
    lca = lowest_common_ancestor(root, "4", "7")
    print(f"   LCA of 4 and 7: {lca.name if lca else None}")

    print("\n7. Complete Binary Tree (not perfect)")
    root = build_complete_tree()
    print(f"   calculate_height: {calculate_height(root)}")
    print(f"   count_nodes: {count_nodes(root)}")
    print(f"   count_leaves: {count_leaves(root)}")
    print(f"   is_perfect_binary_tree: {is_perfect_binary_tree(root)}")
    print(f"   is_complete_binary_tree: {is_complete_binary_tree(root)}")

    print("\n8. Incomplete Binary Tree")
    root = build_incomplete_tree()
    print(f"   calculate_height: {calculate_height(root)}")
    print(f"   count_nodes: {count_nodes(root)}")
    print(f"   is_complete_binary_tree: {is_complete_binary_tree(root)}")

    print("\n9. Example Tree (from original)")
    root = build_example_tree()
    print(f"   calculate_height: {calculate_height(root)}")
    print(f"   calculate_node_height('5'): {calculate_node_height(root, '5')}")
    print(f"   count_nodes: {count_nodes(root)}")
    print(f"   count_leaves: {count_leaves(root)}")
    print(f"   is_balanced: {is_balanced(root)}")
    print(f"   is_full_binary_tree: {is_full_binary_tree(root)}")
    print(f"   is_perfect_binary_tree: {is_perfect_binary_tree(root)}")
    print(f"   is_complete_binary_tree: {is_complete_binary_tree(root)}")
    node = find_category(root, "4")
    print(f"   find_category('4'): {node.name if node else None}")
    path = find_path_to_root(root, "8")
    print(f"   find_path_to_root('8'): {path}")
    lca = lowest_common_ancestor(root, "8", "5")
    print(f"   LCA of 8 and 5: {lca.name if lca else None}")

    print("\n10. Large Tree (stress test)")
    root = build_large_tree(10)
    print(f"   calculate_height: {calculate_height(root)}")
    print(f"   count_nodes: {count_nodes(root)}")
    print(f"   count_leaves: {count_leaves(root)}")
    print(f"   is_balanced: {is_balanced(root)}")
    print(f"   is_full_binary_tree: {is_full_binary_tree(root)}")
    print(f"   is_perfect_binary_tree: {is_perfect_binary_tree(root)}")

    print("\n11. Non-existent Node Tests")
    root = build_example_tree()
    print(f"   find_category('999'): {find_category(root, '999')}")
    print(f"   calculate_node_height('999'): {calculate_node_height(root, '999')}")
    print(f"   find_path_to_root('999'): {find_path_to_root(root, '999')}")

    print("\n" + "=" * 50)
    print("ALL TESTS COMPLETED")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
