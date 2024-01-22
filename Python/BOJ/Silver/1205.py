import sys
input = sys.stdin.readline

n, t, p = map(int, input().split())

if n > 0:
    rank = list(map(int, input().strip().split()))

    if n == p and rank[n-1] >= t:
        print(-1)

    else:
        ans = n + 1
        for i in range(n):
            if rank[i] <= t:
                ans = i + 1
                break
        print(ans)

else:
    print(1)