from collections import deque

n, m, k = map(int, input().split())
list = [[0 for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

max = 0

for i in range(k):
    a, b = map(int, input().split())
    list[a-1][b-1] = "#"


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    list[x][y] = 0
    size = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if list[nx][ny] == "#":
                    size += 1
                    list[nx][ny] = 0
                    queue.append((nx, ny))
    return size

for i in range(n):
    for j in range(m):
        if list[i][j] == "#":
            ans = bfs(i, j)
            if ans > max:
                max = ans

print(max)