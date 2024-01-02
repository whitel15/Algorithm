from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    graph = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[1 for _ in range(102)] for _ in range(102)]
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for i in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, i)
        for a in range(x1, x2 + 1):
            for b in range(y1, y2 + 1):
                if x1 < a < x2 and y1 < b < y2:
                    graph[a][b] = 0
                elif graph[a][b] != 0:
                    graph[a][b] = 1

    cx, cy, ix, iy = 2 * characterX, 2 * characterY, 2 * itemX, 2 * itemY

    dq = deque()
    dq.append((cx, cy))

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            dx = x + direction[i][0]
            dy = y + direction[i][1]

            if dx == ix and dy == iy:
                return (visited[x][y] + 1) // 2
            elif graph[dx][dy] == 1 and visited[dx][dy] == 1:
                visited[dx][dy] += visited[x][y]
                dq.append((dx, dy))

    return answer