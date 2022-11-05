from sys import stdin

A, B, C = map(int, stdin.readline().split())


def solve(A, B):
    if B == 1:
        return A % C
    elif B % 2 == 0:
        y = solve(A, B // 2)
        return y * y % C
    else:
        y = solve(A, (B - 1) // 2)
        return y * y * A % C


print(solve(A, B))
