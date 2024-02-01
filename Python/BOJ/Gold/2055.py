import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
A = deque(list(map(int, input().split())))
ans = 0
is_robot = deque([0 for _ in range(n)])
idx_robot = []

while True:
    ans += 1

    A.rotate(1)
    is_robot.rotate(1)

    is_robot[n-1] = 0

    for i in range(n-2, -1, -1):
        if is_robot[i] and not is_robot[i+1] and A[i+1] > 0:
            is_robot[i] = 0
            is_robot[i+1] = 1
            A[i + 1] -= 1

    is_robot[n-1] = 0

    if A[0] != 0:
        A[0] -= 1
        is_robot[0] = 1

    if A.count(0) >= k:
        break


print(ans)
