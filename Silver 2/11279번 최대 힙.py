import heapq
from sys import stdin

N = int(stdin.readline().rstrip())
heap = []

for _ in range(N):
    x = int(stdin.readline().rstrip())
    if x:
        heapq.heappush(heap, [-x, x])
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

