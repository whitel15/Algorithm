import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
miro = []
visited = [[0 for _ in range(c)] for _ in range(r)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
F = []
dq = deque()

for _ in range(r):
    miro.append(list(input().rstrip()))

for i in range(r):
    for j in range(c):
        if miro[i][j] == 'J':
            dq.append((i, j))
            visited[i][j] = 1
        elif miro[i][j] == 'F':
            F.append([i, j])
            visited[i][j] = "F"

for i in range(len(F)):
    dq.append((F[i][0], F[i][1]))


def bfs():
    while dq:
        x, y = dq.popleft()
        if visited[x][y] == "F":
            flag = "fire"
        else:
            flag = visited[x][y]
        for i in range(4):
            dx = x + direction[i][0]
            dy = y + direction[i][1]
            if 0 <= dx < r and 0 <= dy < c:
                if flag == "fire":
                    if miro[dx][dy] != "#" and visited[dx][dy] != "F":
                        visited[dx][dy] = "F"
                        dq.append((dx, dy))
                else:
                    if miro[dx][dy] == "." and visited[dx][dy] == 0:
                        visited[dx][dy] = visited[x][y] + 1
                        dq.append((dx, dy))

            else:
                if flag != "fire":
                    return visited[x][y]
    return "IMPOSSIBLE"


print(bfs())
