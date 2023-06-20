from queue import PriorityQueue

N = int(input())

A = PriorityQueue()
B = PriorityQueue()
isZ = 0
ans = 0

for i in range(N):
    k = int(input())
    if k > 1:
        A.put(k * -1)
    elif k == 1:
        ans += 1
    elif k == 0:
        isZ += 1
    else:
        B.put(k)

while A.qsize() > 1:
    ans += A.get() * A.get()

if A.qsize() != 0:
    ans += A.get() * -1

while B.qsize() > 1:
    ans += B.get() * B.get()

if B.qsize() != 0:
    if isZ == 0:
        ans += B.get()

print(str(ans))
