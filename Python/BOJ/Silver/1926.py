from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = []
ans = []
visited = [[0 for _ in range(m)] for _ in range(n)]
direction = [(0,1), (0,-1), (-1,0), (1,0)]
for i in range(n):
    paper.append(list(map(int, input().strip().split())))

dq = deque()

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and visited[i][j] == 0:
            size = 0
            dq.append((i, j))
            while dq:
                x, y = dq.popleft()
                visited[x][y] = 1
                size += 1
                for k in range(4):
                    dx = x + direction[k][0]
                    dy = y + direction[k][1]
                    if 0 <= dx < n and 0 <= dy < m and visited[dx][dy] == 0 and paper[dx][dy] == 1:
                        visited[dx][dy] = 1
                        dq.append((dx, dy))
            ans.append(size)

print(len(ans))

if len(ans):
    print(max(ans))
else:
    print(0)