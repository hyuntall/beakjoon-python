from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
maze = []
for _ in range(N):
    maze.append(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
queue = deque([[0, 0, 1]])
visited = [[0, 0]]

while queue:
    x, y, cnt = queue.popleft()
    if x==N-1 and y==M-1:
        print(cnt)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and [nx, ny] not in visited and maze[nx][ny] == '1':
            queue.append([nx, ny, cnt + 1])
            visited.append([nx, ny])