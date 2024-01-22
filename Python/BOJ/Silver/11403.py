import sys
input = sys.stdin.readline

n = int(input())

way = []
visited = [0 for _ in range(n)]

for i in range(n):
    way.append(list(map(int, input().split())))


def dfs(x):
    for i in range(n):
        if way[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(i)


for i in range(n):
    dfs(i)
    for j in range(n):
        print(visited[j], end=' ')
    print()
    visited = [0 for _ in range(n)]