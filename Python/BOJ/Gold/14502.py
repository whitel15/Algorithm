import sys
input = sys.stdin.readline
import copy
from collections import deque

virus = []
move = [[-1, 0], [1, 0], [0, 1], [0, -1]]
n, m = map(int, input().split())
result = 0

for i in range(n):
    virus.append(list(map(int, input().split())))

def bfs():
    uv = copy.deepcopy(virus)
    dq = deque()
    count = 0
    global result
    for i in range(n):
        for j in range(m):
            if uv[i][j] == 2:
                dq.append((i, j))
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            dx = x + move[i][0]
            dy = y + move[i][1]
            if 0 <= dx < n and 0 <= dy < m and uv[dx][dy] == 0:
                uv[dx][dy] = 2
                dq.append((dx, dy))
    for i in range(n):
        for j in range(m):
            if uv[i][j] == 0:
                count += 1
    result = max(result, count)

# 벽 3개 세우기

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if virus[i][j] == 0:
                virus[i][j] = 1
                make_wall(cnt + 1)
                virus[i][j] = 0

make_wall(0)
print(result)