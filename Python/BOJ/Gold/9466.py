import sys
input = sys.stdin.readline
sys.setrecursionlimit(1111111)

t = int(input())

def dfs(x,s):
    global ans
    global k
    check[x] = k
    seq[x] = s
    if seq[num[x]] == 0:
        dfs(num[x],s+1)
    else:
        if check[num[x]] == k:
            ans = ans - s + seq[num[x]] - 1
        else:
            return

for _ in range(t):
    n = int(input())
    num = [0] + list(map(int, input().split()))
    check = [0] * (n+1)
    seq = [0] * (n+1)
    ans = n
    k=1
    for i in range(1, n+1):
        if check[i] == 0:
            dfs(i,1)
            k=k+1
    print(ans)