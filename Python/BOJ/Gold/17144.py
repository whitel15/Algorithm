import sys
input = sys.stdin.readline
from collections import deque

r, c, t = map(int, input().split())

dust = []
gc = 0
result = 2
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(r):
    dust.append(list(map(int, input().split())))

for i in range(r):
    if dust[i][0] == -1:
        gc = i
        break

gc2 = gc + 1

while t > 0:
    t -= 1
    update = deque()
    for i in range(r):
        for j in range(c):
            if dust[i][j] > 0:
                cnt = 0
                for z in range(4):
                    di = i + move[z][0]
                    dj = j + move[z][1]
                    if 0 <= di < r and 0 <= dj < c and dust[di][dj] != -1:
                        cnt += 1
                        update.append((di, dj, dust[i][j] // 5))
                dust[i][j] = dust[i][j] - (dust[i][j] // 5) * cnt

    while update:
        x, y, d = update.popleft()
        dust[x][y] += d

    # 위쪽 순환
    up = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    direct = 0
    x, y = gc, 1
    previous = 0
    while True:
        nx, ny = x + up[direct][0], y + up[direct][1]
        if x == gc and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        dust[x][y], previous = previous, dust[x][y]
        x, y = nx, ny

    # 아래쪽 순환
    up = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direct = 0
    x, y = gc + 1, 1
    previous = 0
    while True:
        nx, ny = x + up[direct][0], y + up[direct][1]
        if x == gc and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        dust[x][y], previous = previous, dust[x][y]
        x, y = nx, ny

    dust[gc][0] = -1
    dust[gc+1][0] = -1


for i in range(r):
    for j in range(c):
        result += dust[i][j]

print(result)
