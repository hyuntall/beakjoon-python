T = int(input())
for _ in range(T):
    N = int(input())
    dp = [1, 2, 4]
    for i in range(3, N):
        dp.append(sum(dp[i-3:i]))
    print(dp[N-1])