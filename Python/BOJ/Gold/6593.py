from collections import deque
import sys
input = sys.stdin.readline

while 1:
    l, r, c = map(int, input().split())

    if l == 0 and r == 0 and c == 0:
        break

    building = []
    direction = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
    visited = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    dq = deque()
    ans = "Trapped!"

    for i in range(l):
        building.append([list(input().strip()) for _ in range(r)])
        temp = input()

    for i in range(l):
        for j in range(r):
            for z in range(c):
                if building[i][j][z] == 'S':
                    dq.append((i, j, z, 0))
                    visited[i][j][z] = 1
                    break

    while dq:
        f, x, y, cnt = dq.popleft()
        if building[f][x][y] == 'E':
            ans = "Escaped in " + str(cnt) + " minute(s)."
            break
        for i in range(6):
            df = f + direction[i][0]
            dx = x + direction[i][1]
            dy = y + direction[i][2]
            if 0 <= df < l and 0 <= dx < r and 0 <= dy < c and visited[df][dx][dy] == 0:
                if building[df][dx][dy] == '.' or building[df][dx][dy] == 'E':
                    visited[df][dx][dy] = 1
                    dq.append((df, dx, dy, cnt + 1))

    print(ans)

