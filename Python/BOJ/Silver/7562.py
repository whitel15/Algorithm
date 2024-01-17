from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
direction = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
ans = []

for _ in range(t):
    l = int(input())
    a, b = map(int, input().split())
    x, y = map(int, input().split())

    visited = [[0 for _ in range(l)] for _ in range(l)]
    cnt = 0
    dq = deque()
    dq.append((a, b, cnt))
    visited[a][b] = 1

    while dq:
        n, m, count = dq.popleft()
        if n == x and m == y:
            ans.append(count)
            break
        for i in range(8):
            dn = n + direction[i][0]
            dm = m + direction[i][1]
            if 0 <= dn < l and 0 <= dm < l and visited[dn][dm] == 0:
                dq.append((dn, dm, count + 1))
                visited[dn][dm] = 1


for i in ans:
    print(i)