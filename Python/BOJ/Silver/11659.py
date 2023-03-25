import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [0]
temp = 0

for i in A:
    temp = temp + i
    S.append(temp)

for j in range(M):
    a, b = map(int, input().split())
    print(S[b]-S[a-1])
