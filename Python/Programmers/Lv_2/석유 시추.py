import sys
sys.setrecursionlimit(1000000)

def solution(land):
    h = len(land)
    w = len(land[0])
    visited = [[0 for _ in range(w)] for _ in range(h)]
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    st = [0 for _ in range(w)]
    cnt = 0
    mw = 0

    def dfs(x, y):
        nonlocal cnt
        nonlocal mw
        visited[x][y] = 1
        for i in range(4):
            dx = x + direction[i][0]
            dy = y + direction[i][1]
            if 0 <= dx < h and 0 <= dy < w and visited[dx][dy] == 0 and land[dx][dy] == 1:
                mw = max(mw, dy)
                cnt += 1
                dfs(dx, dy)

    for i in range(w):
        for j in range(h):
            if visited[j][i] == 0 and land[j][i] == 1:
                cnt += 1
                mw = i
                dfs(j, i)
                for z in range(i, mw + 1):
                    st[z] += cnt
                cnt = 0

    return max(st)