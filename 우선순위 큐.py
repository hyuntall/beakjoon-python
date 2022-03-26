MAX_HEAP_SIZE = 101


class Heap:
    def __init__(self):
        self.arr = [None] * MAX_HEAP_SIZE
        self.heap_count = 0

    # 부모 노드와 우선 순위 비교
    def compare_with_parent(self, index):
        if index <= 1:
            return False
        parent_index = index // 2
        if self.arr[index][0] < self.arr[parent_index][0]:
            return True
        else:
            return False
    # 데이터 삽입
    def insert(self, data):
        self.heap_count += 1
        if self.heap_count == 1:
            self.arr[self.heap_count] = data
            return

        self.arr[self.heap_count] = data
        insert_index = self.heap_count

        # 삽입된 데이터가 부모 노드보다 작으면 스위칭
        while self.compare_with_parent(insert_index):
            parent = insert_index // 2
            self.arr[insert_index], self.arr[parent] = (
                self.arr[parent],
                self.arr[insert_index],
            )

            insert_index = parent
        # print(self.arr[1: self.heap_count + 1])
        return True

    # 자식 노드와 우선 순위 비교
    def compare_with_child(self, index):
        left = 2 * index
        right = 2 * index + 1

        if self.arr[left] == None and self.arr[right] == None:
            return False

        if self.arr[right] == None:
            if self.arr[left][0] < self.arr[index][0]:
                return left
            else:
                return False

        if self.arr[left][0] < self.arr[right][0]:
            return left
        else:
            return right

    # 우선 순위가 가장 빠른 데이터 추출
    def pop(self):
        index = 1
        root = self.arr[1]

        terminal_data = self.arr[self.heap_count]
        self.arr[self.heap_count] = None
        self.arr[index] = terminal_data
        self.heap_count -= 1

        # 말단 데이터를 최상위 노드로 이동 후 자식노드와 비교하며 스위칭
        while True:
            child_index = self.compare_with_child(index)
            if not child_index:
                break

            self.arr[child_index], self.arr[index] = (
                self.arr[index],
                self.arr[child_index],
            )
            index = child_index

        return root[1]


heap = Heap()
heap.insert([9, "JAVA 익히기"])
heap.insert([6, "파이썬 프로젝트 시작하기"])
heap.insert([10, "파이썬 챗봇과정 학습"])
heap.insert([1, "코드메이트에 포스트 작성"])
heap.insert([5, "자료구조 학습"])
heap.insert([2, "모각코 출석"])

print(heap.pop())

print(heap.pop())

print(heap.pop())