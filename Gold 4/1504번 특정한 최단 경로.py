from sys import stdin
import heapq

INF = int(1e9)
def dijkstra(i, goal):
    queue = []
    distance = [INF] * (N+1)
    heapq.heappush(queue, (0, i))
    distance[i] = 0

    while queue:
        dist, index = heapq.heappop(queue)

        if distance[index] < dist:
            continue

        for node_index, node_dist in graph[index]:
            cost = dist + node_dist

            if distance[node_index] > cost:
                distance[node_index] = cost

                heapq.heappush(queue, (cost, node_index))

    # 목표지점까지의 거리를 반환한다
    return distance[goal]



N, E = map(int, stdin.readline().split())

graph = {}

for i in range(1, N+1):
    graph[i] = []

# 각 노드간의 거리를 양방향 그래프로 저장한다.
for _ in range(E):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, stdin.readline().split())

# 1에서 v1, v1에서 v2, v2에서 N까지의 거리와
# 1에서 v2, v2에서 v1, v1에서 N까지의 거리 중 최소를 구한다.
ans = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))

# 이 때 구한 거리가 비정상적으로 크면 v1이나 v2가 없는 것으로 간주한다.
if ans >= INF:
    print(-1)
else:
    print(ans)