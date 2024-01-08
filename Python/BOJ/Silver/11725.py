import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
list = [[] for _ in range(n+1)]
visited = [0 for _ in range(n + 1)]

for i in range(n-1):
    a, b = map(int, input().split())
    list[a].append(b)
    list[b].append(a)


def dfs(node):
    for i in list[node]:
        if visited[i] == 0:
            visited[i] = node
            dfs(i)


dfs(1)

for i in range(2, n+1):
    print(visited[i])