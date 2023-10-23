from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

q = deque()


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not graph[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if graph[i][j]:
            q.append((i, j))

bfs()

print(max(map(max, graph)) - 1)