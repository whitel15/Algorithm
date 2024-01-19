from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [-1 for _ in range(100001)]

dq = deque()
path = []

dq.append((n, 0))

while dq:
    node, cnt = dq.popleft()
    if node == k:
        print(cnt)
        idx = node
        while idx != n:
            path.append(idx)
            idx = visited[idx]
        path.append(n)
        break

    if 0 <= node - 1 < 100001 and visited[node - 1] == -1:
        dq.append((node - 1, cnt + 1))
        visited[node - 1] = node
    if 0 <= node + 1 < 100001 and visited[node + 1] == -1:
        dq.append((node + 1, cnt + 1))
        visited[node + 1] = node
    if 0 <= node * 2 < 100001 and visited[node * 2] == -1 and node < k:
        dq.append((node * 2, cnt + 1))
        visited[node * 2] = node

for i in range(len(path)-1, -1, -1):
    print(path[i], end=" ")