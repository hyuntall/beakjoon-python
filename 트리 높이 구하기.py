class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_tree():
    root = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    root.left = node_2
    root.right = node_3

    node_4 = Node(4)
    node_5 = Node(5)
    node_2.left = node_4
    node_2.right = node_5

    return root


def pre_order(node, depth):
    global height, maxHeightNode
    if node == None:
        return depth
    depth += 1
    if depth > height:
        height = depth
        maxHeightNode = node
    pre_order(node.left, depth)
    pre_order(node.right, depth)


height = 0
root = get_tree()
pre_order(root, 0)
print(f"최대 높이 {height}")
print(f"가장 깊은 레벨의 노드 {maxHeightNode.data}")
