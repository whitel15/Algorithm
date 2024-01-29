import sys
input = sys.stdin.readline
sys.setrecursionlimit(1111111)

n, m = map(int, input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
board = []


for i in range(n):
    board.append(list(input().strip()))


def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        dx = x + int(board[x][y]) * direction[i][0]
        dy = y + int(board[x][y]) * direction[i][1]
        if 0 <= dx < n and 0 <= dy < m and board[dx][dy] != "H" and cnt + 1 > dp[dx][dy]:
            if visited[dx][dy] == 0:
                dp[dx][dy] = cnt + 1
                visited[dx][dy] = 1
                dfs(dx, dy, cnt + 1)
                visited[dx][dy] = 0
            else:
                print(-1)
                exit()


ans = -1
dfs(0, 0, 1)
print(ans)
