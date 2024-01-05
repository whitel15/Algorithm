from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
list = [[] for _ in range(n)]
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
min = 100
max = 0
ans = [1]
dq = deque()

for i in range(n):
    line = input().split()
    for j in line:
        if int(j) < min:
            min = int(j)
        if int(j) > max:
            max = int(j)
        list[i].append(int(j))

for rain in range(min, max + 1):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and list[i][j] > rain:
                cnt += 1
                dq.append((i, j))
                visited[i][j] = 1
                while dq:
                    x, y = dq.popleft()
                    for k in range(4):
                        dx = x + direction[k][0]
                        dy = y + direction[k][1]
                        if 0 <= dx < n and 0 <= dy < n and visited[dx][dy] == 0 and list[dx][dy] > rain:
                            visited[dx][dy] = 1
                            dq.append((dx, dy))

    ans.append(cnt)

ans.sort(reverse=True)

print(ans[0])