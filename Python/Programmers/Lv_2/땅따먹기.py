def solution(land):
    dp = [[0 for _ in range(4)] for _ in range(len(land))]

    for i in range(len(land)):
        for j in range(4):
            if i == 0:
                dp[i][j] = land[i][j]
            else:
                dp[i][j] = max(dp[i - 1][:j] + dp[i - 1][j + 1:]) + land[i][j]

    return max(dp[len(land) - 1])