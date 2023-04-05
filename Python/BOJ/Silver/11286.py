from queue import PriorityQueue
import sys

input = sys.stdin.readline

N = int(input())
queue = PriorityQueue(maxsize=N)

for i in range(N):
    a = int(input())
    if a != 0:
        queue.put((abs(a) - 0.5, a))
    elif a == 0:
        if queue.qsize() != 0:
            print(queue.get()[1])
        elif queue.qsize() == 0:
            print(0)
