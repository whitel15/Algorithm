N = int(input())
t = []

for i in range(N):
    A, B = map(int, input().split())
    t.append((B, A))

t.sort()
last = 0
total = 0

for i in range(N):
    if t[i][1] >= last:
        last = t[i][0]
        total += 1

print(total)
