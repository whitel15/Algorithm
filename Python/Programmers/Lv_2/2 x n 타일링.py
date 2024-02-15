def solution(n):
    dp = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        else:
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

    return dp[n]