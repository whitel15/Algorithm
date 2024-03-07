from collections import deque


def solution(maps):
    answer = []
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    dq = deque()
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    cnt = 0

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and visited[i][j] == 0:
                cnt += int(maps[i][j])
                dq.append((i, j))
                visited[i][j] = 1
                while dq:
                    x, y = dq.popleft()
                    for z in range(4):
                        dx = x + move[z][0]
                        dy = y + move[z][1]
                        if 0 <= dx < len(maps) and 0 <= dy < len(maps[0]) and maps[dx][dy] != "X" and visited[dx][dy] == 0:
                            visited[dx][dy] = 1
                            dq.append((dx, dy))
                            cnt += int(maps[dx][dy])
                answer.append(cnt)
                cnt = 0

    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()

    return answer