import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = map(int, input().split())
A = list(A)

A.sort()

print(A[K-1])