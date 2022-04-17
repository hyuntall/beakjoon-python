from sys import stdin
import heapq

INF = int(1e9)
def dijkstra(i, destination):
    queue = []
    heapq.heappush(queue, (0, i))
    costList = [INF] * (N+1)
    costList[i] = 0

    while queue:
        cost, city = heapq.heappop(queue)

        if costList[city] < cost:
            continue

        for node_city, node_cost in graph[city]:
            new_cost = cost + node_cost

            if costList[node_city] > new_cost:
                costList[node_city] = new_cost

                heapq.heappush(queue, (new_cost, node_city))

    return costList[destination]


N = int(input())
M = int(input())
graph = {}
for i in range(1, N+1):
    graph[i] = []
for _ in range(M):
    start, end, cost = map(int, stdin.readline().split())
    graph[start].append([end, cost])

start_city, destination = map(int, stdin.readline().split())

print(dijkstra(start_city, destination))