import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = []
ans = [0] * N

for i in range(N):
    while B and A[B[-1]] < A[i]:
        ans[B.pop()] = A[i]
    B.append(i)


for i in B:
    ans[i] = -1

for i in range(N):
    print(ans[i],end=" ")
