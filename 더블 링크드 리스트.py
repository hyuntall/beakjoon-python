# 노드 클래스.
# 생성자로 데이터와 포인터를 받는다.
# 포인터가 입력이 안된 경우, 해당 노드가 종단점이라는 의미.
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        # 이전 노드에 대한 포인터와 다음 노드에 대한 포인터 선언
        self.prev = prev
        self.next = next

# 링크드리스트 클래스.
# 클래스 객체 생성시 데이터가 존재하지 않는 노드를 생성한다.
# 해당 노드의 포인터가 바로 Head.
class DoubleLinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None, self.head)
        # head 노드의 다음 노드는 tail 노드
        self.head.next = self.tail
        # 링크드리스트의 노드 개수를 저장하는 변수 size.
        self.size = 0

    # idx 위치에 존재하는 노드를 받아온다.
    def get(self, idx):
        # 입력된 인덱스가 링크드리스트 사이즈보다 클 경우, 오류가 발생.
        if idx >= self.size:
            print("Index Error")
            return None
        # 인덱스가 0인 경우, 헤드를 받아오라는 의미
        if idx == 0:
            return self.head
        if idx == self.size:
            return self.tail
        else:
            node = self.head
            for _ in range(idx):
                node = node.next
            return node

    # 데이터를 링크드리스트 종단점으로 추가한다.
    def appendPrev(self, data):
        if self.size == 0:
            self.head = Node(data)
            self.tail = Node(data, self.head)
            self.head.next = self.tail
        else:
            node = self.head
            # 종단점의 포인터는 None값을 가짐.
            self.head = Node(data, None, self.head)
            node.prev = self.head
        self.size += 1

    def appendNext(self, data):
        if self.size == 0:
            self.head = Node(data)
            self.tail = Node(data, self.head)
            self.head.next = self.tail
        else:
            node = self.tail.prev
            new_node = Node(data,node,self.tail)
            node.next = new_node
            self.tail.prev = new_node
        self.size += 1

    # 데이터를 idx 위치에 추가한다.
    def insert(self, value, idx):
        if self.size == 0:
            self.head = Node(value)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        # idx가 0이라는건, Head 자리에 새로운 데이터를 넣는다는 의미.
        else:
            node = self.get(idx)

            if node == None:
                return
            if node == self.head:
                self.appendPrev(value)
            elif node == self.tail:
                self.appendNext(value)
            else:
                node_prev = node.prev
                newNode = Node(value,node_prev,node)
                node_prev.next = newNode
                node.prev = newNode
        self.size += 1

    # idx 위치의 노드를 삭제한다.
    def delete(self, idx):
        if self.size == 0:
            print("Empty Linked List")
            return
        else:
            node = self.get(idx)
            if node == None:
                return
            elif node == self.head:
                node = self.head
                self.head = self.head.next
            elif node == self.tail:
                node = self.tail
                self.tail = self.tail.prev
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            del(node)
            self.size -= 1

    def print_linked_list(self):
        node = self.head
        while node:
            if node.next != None:
                print(node.data, "-> ", end="")
                node = node.next
            else:
                print(node.data)
                node = node.next

LL = DoubleLinkedList()
LL.print_linked_list()
LL.appendNext("Data1")
LL.print_linked_list()
LL.appendNext("Data2")
LL.print_linked_list()
LL.appendPrev("Data3")
LL.print_linked_list()
LL.insert("Data4", 1)
LL.print_linked_list()

LL.delete(0)
LL.print_linked_list()
LL.delete(2)
LL.print_linked_list()
LL.delete(0)
LL.print_linked_list()