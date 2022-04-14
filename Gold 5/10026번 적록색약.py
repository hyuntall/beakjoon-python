from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    queue = deque([[i, j]])
    visited[i][j] = 0
    while queue:
        x, y = queue.popleft()
        for a in range(4):
            nx = x + dx[a]
            ny = y + dy[a]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] and picture[nx][ny] == picture[i][j]:
                queue.append([nx, ny])
                visited[nx][ny] = 0


N = int(input())
picture = []
visited = [[1] * N for i in range(N)]
for _ in range(N):
    picture.append(list(input()))

cntA = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            bfs(i, j)
            cntA += 1

for i in range(N):
    for j in range(N):
        if picture[i][j] == 'R':
            picture[i][j] = 'G'

visited = [[1] * N for i in range(N)]

cntB = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            bfs(i, j)
            cntB += 1

print(cntA, cntB)
