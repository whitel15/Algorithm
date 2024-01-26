import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
BW = [[] for _ in range(n)]
ans = -1

for i in range(n):
    line = input()
    for j in range(m):
        BW[i].append(int(line[j]))

dq = deque()
dq.append((0, 0, 0))
visited[0][0][0] = 1

while dq:
    x, y, w = dq.popleft()
    if x == n - 1 and y == m - 1:
        ans = visited[x][y][w]
        break
    for z in range(4):
        dx = x + direction[z][0]
        dy = y + direction[z][1]
        if 0 <= dx < n and 0 <= dy < m:
            if visited[dx][dy][w] == 0 and BW[dx][dy] == 0:
                visited[dx][dy][w] = visited[x][y][w] + 1
                dq.append((dx, dy, w))
            elif w == 0 and BW[dx][dy] == 1:
                visited[dx][dy][w + 1] = visited[x][y][w] + 1
                dq.append((dx, dy, 1))

print(ans)