import heapq
from sys import stdin
heap = []
N = int(input())
for _ in range(N):
    A = int(stdin.readline())
    # 0보다 큰 수 입력 받으면 배열에 삽입
    if A:
        heapq.heappush(heap, A)
    else:
        # 0을 입력 받으면 배열 내 가장 작은 수 출력
        if heap:
            print(heapq.heappop(heap))
        # 배열의 크기가 0이면 0 출력
        else:
            print(0)
