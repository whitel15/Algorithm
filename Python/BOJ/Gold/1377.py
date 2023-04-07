import sys
input = sys.stdin.readline

N = int(input())
A = [0] * N
B = [0] * N
max = 0

for i in range(N):
    A[i] = (int(input()), i)
    B[i] = A[i]

A.sort()

for i in range(N):
    if A[i][1] - B[i][1] > max:
        max = A[i][1] - B[i][1]

print(max+1)