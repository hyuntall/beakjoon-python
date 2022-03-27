N = int(input())
dp = [0]*(N+1)

# i가 1이 되기 위한 연산 횟수를 구함
for i in range(2, N+1):
    # i는 i-1보다 최대 연산횟수 1회가 많음
    dp[i] = dp[i-1] + 1
    # i가 2혹은 3으로 나누어 떨어지면 -1이랑 연산횟수 비교
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%2==0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[N])

# 점화식: dp[i] = min(dp[i//3]+1, dp[i//2]+1, dp[i-1]+1)