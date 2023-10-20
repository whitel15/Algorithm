from collections import deque

n, m = map(int, input().split())

war = []

nx = [0, 0, 1, -1]
ny = [-1, 1, 0, 0]

ans = [0 for _ in range(2)]

for i in range(m):
    war.append(list(input()))

def bfs(x, y, a):
    queue = deque()
    queue.append((x, y))
    cnt = 1
    war[x][y] = -1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if 0 <= dx < m and 0 <= dy < n:
                if war[dx][dy] == a:
                    cnt += 1
                    war[dx][dy] = -1
                    queue.append((dx, dy))
    return cnt * cnt

for i in range(m):
    for j in range(n):
        if war[i][j] == "W":
            ans[0] += bfs(i, j, "W")
        elif war[i][j] == "B":
            ans[1] += bfs(i, j, "B")

print(ans[0], ans[1])