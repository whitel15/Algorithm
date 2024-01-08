import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
path = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 1


def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])
    while q:
        x, y, ans = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                answer = max(answer, len(ans)+1)
                q.add((nx, ny, ans + board[nx][ny]))


BFS(0, 0)
print(answer)