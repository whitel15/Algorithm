import sys
input = sys.stdin.readline

k, n = map(int, input().split())
cable = []

for _ in range(k):
    cable.append(int(input()))

s, e = 1, max(cable)

while s <= e:
    cnt = 0
    mid = (s + e) // 2
    for i in range(k):
        cnt += cable[i] // mid
    if cnt >= n:
        s = mid + 1
    else:
        e = mid - 1

print(e)