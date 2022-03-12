from sys import maxsize
C, N = map(int , input().split())

# 각 도시 별 비용과 모을 수 있는 인원수 배열에 저장
arr = [list(map(int, input().split())) for _ in range(N)]
# 동적 프로그래밍을 위한 리스트 생성
dp = [0] + [maxsize] * (C+100)

# 각 도시마다 반복
for cost, customer in arr:
    # 현재 인원수를 모으는 비용은
    # (현재 인원수 - 현재 도시에서 모을 수 있는 인원수)의 비용 + 현재 도시의 비용
    # 도시마다 반복하면서 더 작은 값들로 수정해준다.
    for cur_customer in range(customer, C + 101):
        dp[cur_customer] = min(dp[cur_customer], dp[cur_customer-customer] + cost)

print(min(dp[C:C+101]))

# 점화식:
# dp[n명 모으는데 필요한 비용] =
# min(dp[n명 모으는데 필요한 비용],dp[n명 모으는 비용-현재 방문한 도시가 모으는 인원]+해당 도시에서 드는 비용)
# 아직 dp는 내겐 너무 어려운 것 같다