import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maxV = -int(1e9)
minV = int(1e9)


def dfs(i, arr):
    global add, sub, mul, div, maxV, minV
    if i == n:
        maxV = max(maxV, arr)
        minV = min(minV, arr)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, arr + num[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, arr - num[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, arr * num[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(arr / num[i]))
            div += 1


dfs(1, num[0])
print(maxV)
print(minV)
