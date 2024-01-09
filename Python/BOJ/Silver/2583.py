from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

m, n, k = map(int, input().split())
rec = []
board = [[0 for _ in range(n)] for _ in range(m)]
dq = deque()
nx = [0, 0, 1, -1]
ny = [1, -1, 0, 0]
ans = []

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    a1 = m - y1 - 1
    b1 = x1
    a2 = m - y2
    b2 = x2 - 1
    for a in range(a2, a1+1):
        for b in range(b1, b2+1):
            board[a][b] = 1

for i in range(m):
    for j in range(n):
        cnt = 1
        if board[i][j] == 0:
            board[i][j] = 1
            dq.append((i, j))
            while dq:
                x, y = dq.popleft()
                for k in range(4):
                    dx = x + nx[k]
                    dy = y + ny[k]
                    if 0 <= dx < m and 0 <= dy < n and board[dx][dy] == 0:
                        board[dx][dy] = 1
                        cnt += 1
                        dq.append((dx, dy))
            ans.append(cnt)

ans.sort()

print(len(ans))
for i in range(len(ans)):
    print(ans[i], end = " ")