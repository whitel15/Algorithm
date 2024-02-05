import sys
input = sys.stdin.readline

n, k = map(int, input().split())
wt = []
vl = []
for _ in range(n):
    w, v = map(int, input().split())
    wt.append(w)
    vl.append(v)

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n + 1):
    for j in range(k + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif wt[i - 1] <= j:
            dp[i][j] = max(vl[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][k])
