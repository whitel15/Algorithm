import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0 for _ in range(k+1)]

for i in range(k+1):
    if i == 0:
        dp[i] = 1
    elif i == 1:
        dp[i] = n
    elif i > n//2:
        dp[i] = dp[n - i]
    else:
        dp[i] = (dp[i - 1] * (n - i + 1) // i)

print(dp[k] % 10007)
