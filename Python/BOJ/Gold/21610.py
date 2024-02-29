import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
direction = {1 : (0, -1), 2 : (-1, -1), 3 : (-1, 0), 4 :(-1, 1), 5 : (0, 1), 6 : (1, 1), 7 : (1, 0), 8 : (1, -1)}
ans = 0
cloud = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]

for i in range(n):
    board.append(list(map(int, input().split())))

for _ in range(m):
    copy = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    visit = [[0 for _ in range(n)] for _ in range(n)]
    d, s = map(int, input().split())
    for i in range(len(cloud)):
        cloud[i][0] = (cloud[i][0] + direction[d][0] * s) % n
        cloud[i][1] = (cloud[i][1] + direction[d][1] * s) % n
        board[cloud[i][0]][cloud[i][1]] += 1
        visit[cloud[i][0]][cloud[i][1]] = 1

    for i in range(len(cloud)):
        x, y = cloud[i][0], cloud[i][1]
        cnt = 0
        for j in range(4):
            dx = x + copy[j][0]
            dy = y + copy[j][1]
            if 0 <= dx < n and 0 <= dy < n and board[dx][dy] != 0:
                cnt += 1
        board[x][y] += cnt

    new_cloud = []
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0 and board[i][j] >= 2:
                board[i][j] -= 2
                new_cloud.append([i, j])
    cloud = new_cloud

for i in range(n):
    for j in range(n):
        ans += board[i][j]

print(ans)