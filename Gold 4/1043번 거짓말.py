from collections import deque
from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
truthArr = list(map(int, input().split()))
# 진실을 알고있는 사람의 인원 수
truthNum = truthArr[0]
# 진실을 알고있는 사람들의 리스트
truth = truthArr[1:]
ans = 0
graph = {}
visited = []
edArr = []


def addTruth(n):
    queue = deque([n])
    visited = [n]
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            # 해당 참석자와 만났던 사람들을 연쇄로 모두 truth에 저장
            if i not in visited:
                queue.append(i)
                visited.append(i)
                truth.append(i)


for _ in range(M):
    peopleArr = list(map(int, input().split()))
    # 파티의 참석한 인원 수
    peopleNum = peopleArr[0]
    # 파티에 참석한 인원 리스트
    people = peopleArr[1:]

    for i in range(peopleNum):
        # 파티에서 만난 사람들의 연결 관계를 저장
        if people[i] in graph:
            graph[people[i]].extend(people[:i] + people[i + 1:])
        else:
            graph[people[i]] = people[:i] + people[i + 1:]

    # 파티별 참석자들 내역 리스트에 저장
    edArr.append(people)

for i in graph:
    # 파티에 참석한 전체 사람들 중 진실을 아는 사람이 있으면
    if i in truth:
        # 그 사람이 만났던 사람들을 연쇄적으로 truth에 추가
        addTruth(i)

truth = set(truth)

for ed in edArr:
    # 전체 파티 내역을 검사
    possible = True
    for i in ed:
        if i in truth:
            possible = False
            break
    # 파티 중에 진실을 알고 있는 사람이 없는 파티의 갯수만 출력
    if possible:
        ans += 1

print(ans)
