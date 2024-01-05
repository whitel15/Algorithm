from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

nx = [-1, -1, -1, 0, 0, 1, 1, 1]
ny = [-1, 0, 1, -1, 1, -1, 0, 1]
ans = []


def dfs(x, y):
    visited[x][y] = 1
    for i in range(8):
        dx = x + nx[i]
        dy = y + ny[i]
        if 0 <= dx < h and 0 <= dy < w and visited[dx][dy] == 0 and list[dx][dy] == 1:
            dfs(dx, dy)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    list = [[] for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    cnt = 0
    for i in range(h):
        line = input().split()
        for j in line:
            list[i].append(int(j))

    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and list[i][j] == 1:
                dfs(i, j)
                cnt += 1

    ans.append(cnt)

for i in ans:
    print(i)