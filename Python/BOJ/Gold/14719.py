import sys
input = sys.stdin.readline

h, w = map(int, input().split())
A = list(map(int, input().split()))
rain = [[0 for _ in range(w)] for _ in range(h)]
ans = 0

for i in range(len(A)):
    for j in range(A[i]):
        rain[h - j - 1][i] = 1

for i in range(h):
    p = []
    for j in range(w):
        if rain[h - i - 1][j] == 1:
            p.append(j)
    if len(p) > 1:
        a = []
        for m in range(len(p)-1):
            a.append(p[m+1]-p[m])
        for m in a:
            if m > 1:
                ans += m - 1

print(ans)
