from sys import stdin
from collections import deque

n = int(input())
nodeList = list(map(int, stdin.readline().split()))
m = int(input())

graph = {}
for i in range(n):
    # 삭제할 노드를 제외하고 노드 간의 관계 그래프를 생성
    if i == m or nodeList[i] == m:
        continue
    if nodeList[i] in graph:
        graph[nodeList[i]].append(i)
    else:
        graph[nodeList[i]] = [i]

def dfs(node):
    queue = deque([node])
    sum = 0
    # 루트 노드부터 돌면서
    # 더 연결할 노드가 없으면
    # 리프 노드로 간주하고 +1
    while queue:
        q = queue.popleft()
        if q in graph:
                queue += graph[q]
        else:
            sum += 1
    return sum

# 삭제한 노드 중에 루트 노드가 있는지 검사
if -1 in graph:
    print(dfs(-1))
else:
    print(0)


# 후기 :
# 처음 문제를 읽고 전혀 어렵다고 느끼지 못하고
# 로직도 머릿속에서 다 생각났는데 몇시간째 풀지 못했다.
# 처음엔 재귀함수, 후엔 dfs로 접근 했는데도 결국 틀렸다.
# 결국 찾아보니 사소한 차이가 계속해서 답을 틀리게 만들었었다...
# 분명 쉬운 문제인데 못 푼 내가 원망스럽고 바보같이 느껴진다