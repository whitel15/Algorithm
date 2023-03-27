import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mylist = list(map(int, input().split()))
sum = [0] * N
C = [0] * M
sum[0] = mylist[0]
num = 0

for i in range(1, N):
    sum[i] = sum[i-1] + mylist[i]

for i in range(N):
    r = sum[i] % M
    if r == 0:
        num += 1
    C[r] += 1

for i in range(M):
    if C[i] > 1:
        num += (C[i] * (C[i] - 1) // 2)

print(num)