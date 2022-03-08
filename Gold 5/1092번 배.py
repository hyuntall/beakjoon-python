from sys import stdin
n = int(input())
crane = sorted(list(map(int, stdin.readline().split())), reverse=True)
m = int(input())
box = sorted(list(map(int, stdin.readline().split())), reverse=True)

carried = [0] * m
carring = [0] * n
# 상자 무게가 크레인 최대 적재 무게보다 크면 -1
if max(crane) < max(box):
    print(-1)
else:
    time = 0
    # 모든 박스를 옮길때까지
    while sum(carried) != m:
        # 크레인마다 시도
        for i in range(n):
            # 적재한 박스가 전체 박스보다 클 수 없음
            while carring[i] < len(box):
                # 현재 박스가 이미 재적중이지 않으며, 현재 크레인으로 재적 가능한 무게일 때
                if not carried[carring[i]] and crane[i] >= box[carring[i]]:
                    # 해당 박스 재적 표시
                    carried[carring[i]] = 1
                    # 다음 크레인으로 이동
                    carring[i] += 1
                    break
                # 박스가 재적중이거나 박스가 재적 가능한 무게보다 클 때
                # 다음 크레인으로 이동
                carring[i] += 1
        # 1분 추가
        time += 1

    print(time)

# 총평:
# 시간초과를 해결하는 부분에서 많이 애를 먹었다.
# box 리스트에서 옮긴 박스는 remove 하는 방식으로 접근했으나
# remove의 시간복잡도가 n이기 때문에 시간초과가 났다.
# 도저히 감이 잡히지 않아 다른 분들이 풀이한 것을 보면서
# 해결했기 때문에 솔직히 스스로의 힘만으로는 풀었다고 떳떳하게 말하지 못할 것 같다.
# 나중에 다시 풀어봐야겠다.