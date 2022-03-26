from collections import deque

# n과 target의 케빈 베이컨의 수를 구하는 함수
def findFreinds(n, target):
    # 큐 안에 기준이 될 사람과 연결횟수 삽입
    queue = deque([[n, 0]])
    visited = [n]
    while queue:
        q, cnt = queue.popleft()
        # 찾고자 하는 친구를 찾으면 연결횟수 리턴
        if q == target:
            return cnt
        for i in graph[q]:
            if i not in visited:
                # 관계 하나씩 건널 때마다 연결횟수 +1
                queue.append([i, cnt + 1])
                visited.append(i)


N, M = map(int, input().split())
graph = {}
for i in range(1, N + 1):
    graph[i] = set()

# A와 B의 관계를 입력받아 무방향 그래프 생성
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].add(B)
    graph[B].add(A)

cntList = []
# 한명씩 조사
for i in graph:
    sumCnt = 0
    for j in graph:
        # 본인을 제외한 모두와의 케빈 베이컨의 수 합을 구함
        if i == j:
            continue
        sumCnt += findFreinds(i, j)
    cntList.append(sumCnt)

print(cntList.index(min(cntList)) + 1)