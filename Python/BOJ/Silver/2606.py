from collections import deque

n = int(input())
m = int(input())

net = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

vi = []

def bfs(a):
    queue = deque()
    queue.append(a)
    cnt = 0
    while queue:
        x = queue.popleft()
        vi.append(x)
        for i in net[x]:
            if i not in vi:
                cnt += 1
                queue.append(i)
                vi.append(i)

    return cnt


print(bfs(1))