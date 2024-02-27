import sys
input = sys.stdin.readline

n, m = map(int, input().split())
money = []
for i in range(n):
    money.append(int(input()))

s, e = max(money), sum(money)

while s <= e:
    mid = (s + e) // 2
    remain = mid
    cnt = 1
    for i in range(n):
        if money[i] <= remain:
            remain -= money[i]
        else:
            remain = mid - money[i]
            cnt += 1

    if cnt <= m:
        e = mid - 1
    else:
        s = mid + 1

print(s)