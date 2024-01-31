import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
forest = []
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[0 for _ in range(c)] for _ in range(r)]
dq = deque()
Gx = 0
Gy = 0

for _ in range(r):
    forest.append(list(input().strip()))

for i in range(r):
    for j in range(c):
        if forest[i][j] == "*":
            dq.append((i, j, "w"))
            visited[i][j] = "w"
        elif forest[i][j] == "S":
            Gx = i
            Gy = j

dq.append((Gx, Gy, 1))
visited[Gx][Gy] = 1
ans = "KAKTUS"


def dfs():
    global ans
    while dq:
        x, y, flag = dq.popleft()
        for i in range(4):
            dx = x + direction[i][0]
            dy = y + direction[i][1]
            if 0 <= dx < r and 0 <= dy < c and forest[dx][dy] != "X":
                if flag == "w":
                    if forest[dx][dy] != "D" and visited[dx][dy] != "w":
                        visited[dx][dy] = "w"
                        dq.append((dx, dy, "w"))
                else:
                    if forest[dx][dy] == "D":
                        ans = flag
                        return
                    if forest[dx][dy] != "*" and visited[dx][dy] == 0:
                        visited[dx][dy] = flag + 1
                        dq.append((dx, dy, flag + 1))

dfs()
print(ans)
