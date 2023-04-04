from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque([])
for i in range(1,N+1):
    queue.append(i)

for i in range(N-1):
    queue.popleft()
    a = queue.popleft()
    queue.append(a)

print(queue.pop())