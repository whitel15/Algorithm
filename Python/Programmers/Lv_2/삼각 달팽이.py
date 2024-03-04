def solution(n):
    direct = {0: (1, 0), 1: (0, 1), 2: (-1, -1)}
    answer = []
    dal = [[0 for _ in range(n)] for _ in range(n)]
    v = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 1
    d = 0
    x, y = -1, 0
    while cnt <= n * (n + 1) // 2:
        dx = x + direct[d][0]
        dy = y + direct[d][1]
        if 0 <= dx < n and 0 <= dy < n and v[dx][dy] == 0:
            x = dx
            y = dy
            dal[x][y] = cnt
            v[dx][dy] = 1
            cnt += 1
        else:
            d = (d + 1) % 3

    for i in range(n):
        for j in range(n):
            if dal[i][j] != 0:
                answer.append(dal[i][j])

    return answer