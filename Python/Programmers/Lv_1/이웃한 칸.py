def solution(board, h, w):
    answer = 0

    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for i in range(4):
        dx = h + direction[i][0]
        dy = w + direction[i][1]
        if 0 <= dx < len(board) and 0 <= dy < len(board[0]):
            if board[h][w] == board[dx][dy]:
                answer += 1

    return answer