from sys import stdin
import heapq

INF = int(1e9)
def dijkstra(i):
    queue = []
    heapq.heappush(queue, (0, i))
    distance = [INF] * (V+1)
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

    return distance

V, E = map(int, stdin.readline().split())
graph = {}
for i in range(1, V+1):
    graph[i] = []

K = int(input())
for _ in range(E):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append([v, w])

ans = dijkstra(K)
for i in ans[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)