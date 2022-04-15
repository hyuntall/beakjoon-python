N = int(input())
ans = 0

while N >= 5:
    ans += N//5

    N //= 5

print(ans)

# 풀이:
# 뒷자리에 0을 구하려면 N! 안에 있는 5의 갯수를 구한다.