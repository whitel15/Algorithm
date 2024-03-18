def solution(rows, columns, queries):
    answer = []
    num = 1
    board = [[0 for _ in range(columns)] for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            board[i][j] = num
            num += 1

    for i in queries:
        x1, y1, x2, y2 = i[0] - 1, i[1] - 1, i[2] - 1, i[3] - 1
        a = []
        for j in range(y1, y2 + 1):
            a.append(board[x1][j])
            if len(a) == 1:
                continue
            else:
                board[x1][j] = a[-2]

        for j in range(x1 + 1, x2 + 1):
            a.append(board[j][y2])
            board[j][y2] = a[-2]

        for j in range(y2 - 1, y1 - 1, -1):
            a.append(board[x2][j])
            board[x2][j] = a[-2]

        for j in range(x2 - 1, x1 - 1, -1):
            a.append(board[j][y1])
            board[j][y1] = a[-2]

        answer.append(min(a))

    return answer