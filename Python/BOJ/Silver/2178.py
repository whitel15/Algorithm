from collections import deque

n, m = map(int, input().split())

miro = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    miro.append(list(map(int, input().rstrip())))

cnt = 1

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if miro[nx][ny] == 1:
                    if nx == n-1 and ny == m-1:
                        return miro[x][y] + 1
                        break
                    else:
                        queue.append((nx, ny))
                        miro[nx][ny] += miro[x][y]


print(bfs(0, 0))