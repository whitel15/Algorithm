def solution(n):
    answer = 0

    dp = [0 for _ in range(n + 1)]

    for i in range(n + 1):
        if i == 0:
            dp[i] = 0
        elif i == 1:
            dp[i] = 1
        else:
            dp[i] = (dp[i - 2] + dp[i - 1]) % 1234567

    answer = dp[n]

    return answer