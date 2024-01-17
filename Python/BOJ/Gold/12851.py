from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

visited = [0 for _ in range(100001)]

count = 0
ans = 0
way = 0

dq = deque()
dq.append((n, count))

while dq:
    locate, cnt = dq.popleft()

    if locate == k and visited[locate] == 0:
        ans = cnt
        way += 1

    if locate == k and visited[locate] == 1 and ans == cnt:
        way += 1

    visited[locate] = 1

    if 0 <= locate - 1 < 100001 and visited[locate - 1] == 0:
        dq.append((locate - 1, cnt + 1))
    if 0 <= locate + 1 < 100001 and visited[locate + 1] == 0:
        dq.append((locate + 1, cnt + 1))
    if 0 <= locate * 2 < 100001 and visited[locate * 2] == 0:
        dq.append((locate * 2, cnt + 1))


print(ans)
print(way)