from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
box = []
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(n):
    box.append(list(map(int, input().strip().split())))

dq = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            dq.append((i, j, 0))

while dq:
    x, y, cnt = dq.popleft()
    for i in range(4):
        dx = x + direction[i][0]
        dy = y + direction[i][1]
        if 0 <= dx < n and 0 <= dy < m:
            if box[dx][dy] == 0:
                box[dx][dy] = 1
                dq.append((dx, dy, cnt + 1))

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            cnt = -1

print(cnt)