from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
a, b = map(int, input().split())
m = int(input())
fam = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
answer = -1

for i in range(m):
    x, y = map(int, input().split())
    fam[x].append(y)
    fam[y].append(x)

def dfs(node, count):
    global answer
    visited[node] = 1
    for i in fam[node]:
        if visited[i] == 0:
            if i == b:
                answer = count + 1
                return answer
            else:
                dfs(i, count + 1)

def bfs():
    global answer
    dq = deque()
    dq.append((a, 0))
    while dq:
        node, count = dq.popleft()
        visited[node] = 1
        for i in fam[node]:
            if visited[i] == 0:
                if i == b:
                    answer = count + 1
                    return answer
                else:
                    dq.append((i, count + 1))


bfs()

print(answer)