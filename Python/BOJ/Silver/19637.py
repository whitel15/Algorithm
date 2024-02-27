import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pr = []
limit = []
s = {}

for i in range(n):
    a, b = input().split(" ")
    if int(b) not in s:
        s[int(b)] = 0
        pr.append(a)
        limit.append(int(b))

for _ in range(m):
    num = int(input())
    low, high = 0, len(limit) - 1
    idx = 0
    while low <= high:
        mid = (low + high) // 2
        if num == limit[mid]:
            idx = mid
            break
        elif num < limit[mid]:
            high = mid - 1
        else:
            low = mid + 1
            idx = low
    print(pr[idx])