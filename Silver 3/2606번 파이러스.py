from collections import deque

N = int(input())
M = int(input())
graph = {}

for _ in range(M):
    A, B = map(int, input().split())
    # 컴퓨터 A와 B의 관계를 딕셔너리 안에 그래프 저장
    if A in graph:
        graph[A].append(B)
    else:
        graph[A] = [B]
    if B in graph:
        graph[B].append(A)
    else:
        graph[B] = [A]

# 1번 컴퓨터부터 탐색
queue = deque([1])
visited = [1]
cnt = 0
# 더 이상 연결된 컴퓨터가 없을 때 까지 탐색
while queue:
    q = queue.popleft()
    if q in graph:
        for i in graph[q]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
                cnt += 1
# 탐색된 컴퓨터의 갯수 출력
print(cnt)