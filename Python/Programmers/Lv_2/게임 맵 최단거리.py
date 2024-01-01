from collections import deque


def solution(maps):
    answer = -1
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    queue = deque()

    n = len(maps)
    m = len(maps[0])
    visit = [[0 for _ in range(m)] for _ in range(n)]

    queue.append((0, 0, 1))
    visit[0][0] = 1

    while queue:
        x, y, tmp = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visit[nx][ny] == 0:
                queue.append((nx, ny, tmp + 1))
                visit[nx][ny] = 1

                if nx == n - 1 and ny == m - 1:
                    answer = tmp + 1

    return answer