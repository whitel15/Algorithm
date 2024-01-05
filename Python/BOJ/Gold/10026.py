from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
visited = [[0 for _ in range(n)] for _ in range(n)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

list = [[] for _ in range(n)]
dq = deque()

for i in range(n):
    line = input().strip()
    for j in line:
        list[i].append(j)

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dq.append((i, j))
            visited[i][j] = 1
            while dq:
                x, y = dq.popleft()
                for k in range(4):
                    dx = x + direction[k][0]
                    dy = y + direction[k][1]
                    if 0 <= dx < n and 0 <= dy < n and list[dx][dy] == list[i][j] and visited[dx][dy] == 0:
                        visited[dx][dy] = 1
                        dq.append((dx, dy))
            cnt += 1

print(cnt)
visited = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dq.append((i, j))
            visited[i][j] = 1
            while dq:
                x, y = dq.popleft()
                for k in range(4):
                    dx = x + direction[k][0]
                    dy = y + direction[k][1]
                    if 0 <= dx < n and 0 <= dy < n and visited[dx][dy] == 0:
                        if list[x][y] == 'R' or list[x][y] == 'G':
                            if list[dx][dy] == 'R' or list[dx][dy] == 'G':
                                visited[dx][dy] = 1
                                dq.append((dx, dy))
                        else:
                            if list[x][y] ==list[dx][dy]:
                                visited[dx][dy] = 1
                                dq.append((dx, dy))

            cnt += 1

print(cnt)