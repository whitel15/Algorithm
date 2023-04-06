import sys
input = sys.stdin.readline

N = int(input())
ans = [0] * N
s = N-1

for i in range(N):
    ans[i] = int(input())

while s != 0:
    for i in range(s):
        if ans[i] > ans[i + 1]:
            tmp = ans[i + 1]
            ans[i + 1] = ans[i]
            ans[i] = tmp
    s -= 1

for i in range(N):
    print(ans[i])
