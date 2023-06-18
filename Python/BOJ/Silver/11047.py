N, K = map(int, input().split())
ans = 0

A = [0] * N

for i in range(N):
    A[i] = int(input())

for i in range(N - 1, -1, -1):
    if A[i] <= K:
        n = K // A[i]
        ans = ans + n
        K = K % A[i]
        if K == 0:
            print(ans)
            break