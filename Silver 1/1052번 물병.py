n, k = map(int, input().split())
new = 0
while bin(n).count('1') > k:
    L = 2**(bin(n)[::-1].index('1'))
    new += L
    n += L
print(new)

# 총평:
# n개의 물병을 가능한 만큼 합친 갯수와 이진수로 표시한 n의 1의 갯수가 같다.
# 물병을 k개만큼 줄이고 싶다면 이진수에서의 1의 갯수를 줄여야 한다.
# 물의 양도 2배씩 늘어나므로 이진수를 통해 구할 수 있다
# 이진수 n에서 제일 마지막 1을 0으로 만들기 위해 해당 값과 같은 2의 배수를 더해준다
