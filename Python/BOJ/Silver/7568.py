import sys
input = sys.stdin.readline

n = int(input())

D = []
ans = []

for i in range(n):
    w, h = map(int, input().split())
    D.append([w, h])

for i in range(n):
    cnt = 0
    for j in range(n):
        if D[i][0] < D[j][0] and D[i][1] < D[j][1]:
            cnt += 1
    ans.append(cnt+1)

for i in ans:
    print(i, end=" ")