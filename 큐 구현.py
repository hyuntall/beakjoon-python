class Queue:
    # 원형 큐 구현
    def __init__(self, MAX_QUEUE_SIZE):
        self.MAX_QUEUE_SIZE = MAX_QUEUE_SIZE
        self.arr = [None] * self.MAX_QUEUE_SIZE
        # head: 가장 오래된 데이터의 위치
        # tail: 가장 최근 추가된 데이터의 위치
        self.head = 0
        self.tail = 0

    def is_empty(self):
        # 큐가 비었는지 검사
        if self.head == self.tail:
            return True
        return False

    def is_full(self):
        # 큐가 꽉 찼는지 검사
        if (self.tail+1)%(self.MAX_QUEUE_SIZE+1) == self.head:
            return True
        return False

    def enqueue(self, item):
        if self.is_full():
            print("큐에 더 이상 데이터를 넣을 수 없습니다.")
        else:
            self.arr[self.tail] = item
            self.tail = (self.tail+1)%(self.MAX_QUEUE_SIZE+1)

    def dequeue(self):
        if self.is_empty():
            print("큐가 비어있습니다.")
        else:
            self.head = (self.head+1)%(self.MAX_QUEUE_SIZE+1)
            return self.arr[self.head-1]

    def __str__(self):
        return str(self.arr)

N = 7
queue = Queue(N)
for _ in range(N):
    id, time = map(int, input().split())
    queue.enqueue([id,time])

print(queue)
all_time = 0
cur_time = 0
id_arr = []
while not queue.is_empty():
    id, time = queue.dequeue()
    # 남은 근무 시간동안 다음 고객 문의를 처리할 수 없다면
    if cur_time + time>50:
        # 쉬는시간 10분 추가
        all_time += 10
        print(id_arr)
        # 다음 근무 리스트에 해당 고객 추가
        id_arr = [id]
        # 다음 근무 시간에 해당 고객 문의 처리
        cur_time = time

    # 남은 근무 시간동안 다음 고객 문의 처리 가능하다면
    else:
        #현재 근무시간에 다음 고객 문의 처리 시간 추가
        cur_time += time
        id_arr.append(id)
    all_time += time
print(id_arr)

print(f"총 소요시간: {all_time}분")