from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
list = [[] for _ in range(n)]
visited = [0 for _ in range(n)]
dq = deque()
cnt = 0

for i in range(m):
    x, y = map(int, input().split())
    list[x-1].append(y-1)
    list[y-1].append(x-1)

for i in range(n):
    if visited[i] == 0:
        dq.append(i)
        visited[i] = 1
        while dq:
            node = dq.popleft()
            for j in list[node]:
                if visited[j] == 0:
                    visited[j] = 1
                    dq.append(j)
        cnt += 1

print(cnt)