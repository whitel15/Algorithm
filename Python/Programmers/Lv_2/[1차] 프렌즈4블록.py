# 문제를 제대로 읽자

def solution(m, n, board):
    answer = 0
    bo = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            bo[i][j] = board[i][j]

    while True:
        a = 1
        path = set()
        for i in range(0, m - 1):
            for j in range(0, n - 1):
                if bo[i][j] != "X":
                    if bo[i][j] == bo[i][j + 1] and bo[i][j] == bo[i + 1][j] and bo[i][j] == bo[i + 1][j + 1]:
                        path.add((i, j))
                        path.add((i, j + 1))
                        path.add((i + 1, j))
                        path.add((i + 1, j + 1))

        path = list(path)

        if path:
            answer += len(path)
            a = 0
            for z in range(len(path)):
                zx = path[z][0]
                zy = path[z][1]
                bo[zx][zy] = "X"

            for z in range(0, m):
                for q in range(0, n):
                    if bo[z][q] == "X":
                        for v in range(z, 0, -1):
                            bo[v][q] = bo[v - 1][q]
                        bo[0][q] = "X"

        if a:
            return answer