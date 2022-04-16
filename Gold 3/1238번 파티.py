from sys import stdin
from sys import maxsize
import heapq

N, M, X = map(int, stdin.readline().split())
graph = {}
for i in range(1, N+1):
    graph[i] = []
# 각 마을간의 경로와 거리를 그래프에 저장
for _ in range(M):
    start, end, T = map(int, stdin.readline().split())
    graph[start].append([end, T])

def dijkstra(i):
    queue = []
    distance = [maxsize] * (N+1)
    # 현재 위치와 이동한 거리 큐, distance에 저장
    heapq.heappush(queue, (0, i))
    distance[i] = 0

    while queue:
        # 거리가 짧은 마을의 노드 먼저 계산
        dist, village = heapq.heappop(queue)

        # 해당 마을의 거리가 이미 최소 거리이면 스킵
        if distance[village] < dist:
            continue

        # 해당 마을에서 연결된 마을들에 대해
        for node_village, node_dist in graph[village]:
            # 연결된 마을들까지의 거리는 현재 거리 + 해당마을까지의 거리
            cost = dist + node_dist
            # 연결된 마을까지의 거리보다 cost가 작으면 거리 변경
            if distance[node_village] > cost:
                distance[node_village] = cost

                heapq.heappush(queue, (cost, node_village))
    return distance

ans = 0
for i in graph:
    if i == X:
        continue
    # 각 마을에 사는 아이들의 파티 왕복시간 중 최대값 계산
    ans = max(dijkstra(i)[X] + dijkstra(X)[i], ans)

print(ans)