from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cnt = 0
dq = deque()
visited = [0 for _ in range(100001)]
dq.append((n, cnt))

while dq:
    x, count = dq.popleft()
    visited[x] = 1
    if x == k:
        print(count)
        break
    if x + 1 < 100001 and visited[x + 1] == 0:
        dq.append((x + 1, count + 1))
    if 0 <= x - 1 < 100001 and visited[x - 1] == 0:
        dq.append((x - 1, count + 1))
    if x * 2 < 100001 and visited[x * 2] == 0:
        dq.append((x * 2, count + 1))
