import sys
input = sys.stdin.readline

n = int(input())
lose = list(map(int, input().split()))
gain = list(map(int, input().split()))

dp = [[0 for _ in range(100)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(100):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif lose[i-1] <= j:
            dp[i][j] = max(gain[i-1] + dp[i-1][j-lose[i - 1]], dp[i - 1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])
