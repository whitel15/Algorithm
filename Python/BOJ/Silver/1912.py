import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(n):
    dp[i] = max(A[i], A[i] + dp[i-1])

print(max(dp))
