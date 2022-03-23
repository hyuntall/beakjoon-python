class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def set_root(self, data):
        self.root = Node(data)

    def find(self, data):
        if self.find_node_by_recursion(self.root, data) == False:
            return False
        else:
            return True

    def find_node_by_recursion(self, current_node, data):
        if current_node == None:
            return False
        if data == current_node.data:
            return current_node

        if data < current_node.data:
            return self.find_node_by_recursion(current_node.left, data)
        if data > current_node.data:
            return self.find_node_by_recursion(current_node.right, data)

    def insert(self, data):
        if self.root == None:
            self.set_root(data)
        else:
            self.insert_node(self.root, data)

    def insert_node(self, current_node, data):
        if data == current_node.data:
            print(f"이미 {data}값이 존재합니다. 중복된 값은 삽입할 수 없습니다.")
            return
        if data < current_node.data:
            if current_node.left == None:
                current_node.left = Node(data)
            else:
                self.insert_node(current_node.left, data)

        elif data > current_node.data:
            if current_node.right == None:
                current_node.right = Node(data)
            else:
                self.insert_node(current_node.right, data)

    def get_next_node(self, node):
        while node.left != None:
            node = node.left
        return node

    def delete(self, data):
        if self.root == None:
            print("트리에 노드가 존재하지 않습니다.")
        else:
            self.delete_node(None, self.root, data)

    def delete_node(self, parent, current_node, data):
        if current_node == None:
            print(f"트리에 {data}가 존재하지 않습니다.")
            return

        if data < current_node.data:
            self.delete_node(current_node, current_node.left, data)
        elif data > current_node.data:
            self.delete_node(current_node, current_node.right, data)
        else:
            if current_node.left == None and current_node.right == None:
                if data < parent.data:
                    parent.left = None
                else:
                    parent.right = None
            elif current_node.left != None and current_node.right == None:
                if data < parent.data:
                    parent.left = current_node.left
                else:
                    parent.right = current_node.left
            elif current_node.left == None and current_node.right != None:
                if data < parent.data:
                    parent.left = current_node.right
                else:
                    parent.right = current_node.right

            elif current_node.left != None and current_node.right != None:
                next_node = self.get_next_node(current_node.right)

                current_node.data = next_node.data
                self.delete_node(current_node, current_node.right, next_node.data)

def in_order(node):
    if node == None:
        return
    in_order(node.left)
    print(f"{node.data}  ", end="")
    in_order(node.right)

BST = BinarySearchTree()
BST.set_root(7)

BST.insert(3)
BST.insert(1)
BST.insert(5)
BST.insert(10)
BST.insert(8)

BST.insert(4)
BST.insert(12)
BST.insert(15)

BST.delete(10)

in_order(BST.root)