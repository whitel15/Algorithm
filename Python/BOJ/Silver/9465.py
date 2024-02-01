import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    A = []
    ans = []
    for _ in range(2):
        line = input().split()
        A.append([int(x) for x in line])

    dp = [[0 for _ in range(n + 2)] for _ in range(2)]

    for i in range(2, n + 2):
        dp[0][i] = max(A[0][i - 2] + dp[1][i - 1], A[0][i - 2] + dp[1][i - 2])
        dp[1][i] = max(A[1][i - 2] + dp[0][i - 1], A[1][i - 2] + dp[0][i - 2])

    for i in range(2):
        for j in range(n + 2):
            ans.append(dp[i][j])

    print(max(ans))
