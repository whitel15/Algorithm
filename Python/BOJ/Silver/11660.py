import sys
input = sys.stdin.readline

N, M = map(int, input().split())

mylist = [list(map(int, input().split())) for _ in range(N)]

S = [[0 for j in range(N+1)] for i in range(N+1)]

for i in range(N):
    for j in range(N):
        S[i+1][j+1] = S[i+1][j] + S[i][j+1] - S[i][j] + mylist[i][j]

for _ in range(M):
    a, b, c, d = map(int, input().split())
    print(S[c][d]-S[a-1][d]-S[c][b-1]+S[a-1][b-1])
