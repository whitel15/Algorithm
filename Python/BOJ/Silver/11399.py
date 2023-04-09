import sys
input = sys.stdin.readline

changed = False
N = int(input())
A = list(map(int, input().split()))
sum = 0

A.sort()

for i in range(N):
    sum += A[i]*(N-i)

print(sum)
