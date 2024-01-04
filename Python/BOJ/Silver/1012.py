from collections import deque

n = int(input())

direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
dq = deque()
ans = []


def bfs(x, y):
    global visited
    global width
    global length
    dq.append((x, y))
    visited[x][y] = 1
    while dq:
        nx, ny = dq.popleft()
        for i in range(4):
            dx = nx + direction[i][0]
            dy = ny + direction[i][1]
            if 0 <= dx < width and 0 <= dy < length and field[dx][dy] == 1 and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                dq.append((dx, dy))


for i in range(n):
    width, length, k = map(int, input().split())
    field = [[0 for _ in range(length)] for _ in range(width)]
    visited = [[0 for _ in range(length)] for _ in range(width)]
    cnt = 0
    for j in range(k):
        a, b = map(int, input().split())
        field[a][b] = 1
    for x in range(width):
        for y in range(length):
            if field[x][y] == 1 and visited[x][y] == 0:
                bfs(x, y)
                cnt += 1
    ans.append(cnt)

for i in ans:
    print(i)