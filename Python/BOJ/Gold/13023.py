from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
list = [[] for _ in range(n)]
check = [False] * n
ans = False

for i in range(m):
    a, b = map(int, input().split())
    list[a].append(b)
    list[b].append(a)


def DFS(a, depth):
    global ans
    if depth == 5:
        ans = True
        return
    check[a] = True
    for i in list[a]:
        if not check[i]:
            DFS(i, depth + 1)
    check[a] = False


for i in range(n):
    DFS(i, 1)
    if ans:
        break

if ans:
    print(1)
else:
    print(0)

