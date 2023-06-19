from queue import PriorityQueue
import sys
input = sys.stdin.readline

N = int(input())

A = PriorityQueue()
ans = 0

for i in range(N):
    k = int(input())
    A.put(k)

for i in range(N-1):
    k = A.get() + A.get()
    ans = ans + k
    A.put(k)

print(str(ans))