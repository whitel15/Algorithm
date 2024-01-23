from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
land = []
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(n):
    land.append(list(map(int, input().split())))

dq = deque()


def bfs(i, j):
    dq.append((i, j))
    union = []
    union.append((i, j))
    while dq:
        x, y = dq.popleft()
        for z in range(4):
            dx = x + direction[z][0]
            dy = y + direction[z][1]
            if 0 <= dx < n and 0 <= dy < n and l <= abs(land[x][y] - land[dx][dy]) <= r and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                dq.append((dx, dy))
                union.append((dx, dy))
    if len(union) == 1:
        return 0
    result = sum(land[a][b] for a,b in union)//len(union)
    for a, b in union:
        land[a][b] = result
    return 1

day = 0

while 1:
    stop = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                stop += bfs(i, j)
    if stop == 0:
        break
    day += 1

print(day)
