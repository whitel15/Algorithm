import sys
input = sys.stdin.readline
from collections import deque

n, t, g = map(int, input().split())
dq = deque()
visited = [0 for _ in range(100000)]
dq.append((n, 0))
visited[n] = 1
ans = "ANG"

while dq:
    num, cnt = dq.popleft()
    if num == g:
        ans = cnt
        break
    if num < 99999 and cnt < t and visited[num + 1] == 0:
        visited[num + 1] = 1
        dq.append((num + 1, cnt + 1))
    if 0 < num * 2 < 99999 and cnt < t and visited[num * 2 - 10 ** (len(str(num*2))-1)] == 0:
        visited[num * 2 - 10 ** (len(str(num * 2)) - 1)] = 1
        dq.append((num * 2 - 10 ** (len(str(num * 2)) - 1), cnt + 1))

print(ans)
