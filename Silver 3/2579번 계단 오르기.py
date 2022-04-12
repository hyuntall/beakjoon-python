N = int(input())
dp = [0] * (N+1)
point = [0] * (N+1)
for i in range(1, N+1):
    point[i] = int(input())

dp[1] = point[1]
dp[2] = point[1]+point[2]
for i in range(3, N+1):
    dp[i] = max(dp[i-2]+point[i], dp[i-3]+point[i-1]+point[i])

print(dp[-1])
# 점화식
# 마지막 계단과 그 전 계단이 연속적일 때의 경우 dp[i-3]+point[i-1]+point[i]
# 마지막 계단에서 연속적이지 않을 경우 dp[i-2]+point[i]