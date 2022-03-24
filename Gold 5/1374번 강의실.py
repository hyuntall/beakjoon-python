import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())

class_arr = []
for _ in range(n):
    num, start, end = map(int, input().split())
    heappush(class_arr, [start, end, num])

opening_classes = []
start, end, num = heappop(class_arr)
heappush(opening_classes, end)

# 다음 강의 시작 시간이 강의중인 것들의 종료시간보다 늦게 시작하면
# 강의실을 추가할 필요가 없음
# 현재 열려있는 강의들이 끝나기 전에 시작해야할 강의가 있으면 힙에 추가
while class_arr:
    start, end, num = heappop(class_arr)
    if opening_classes[0] <= start:
        heappop(opening_classes)
    heappush(opening_classes, end)

print(len(opening_classes))