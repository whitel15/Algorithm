N, M = map(int, input().split())
A = list(map(int, input().split()))

s = max(A)
e = sum(A)
ans = 0

while s <= e:
    mid = (s + e) // 2
    cnt = 0
    total = 0
    for x in A:
        if total + x > mid:
            cnt += 1
            total = x
        else:
            total += x
    if total:
        cnt += 1
    if cnt <= M:
        e = mid - 1
        ans = mid
    else:
        s = mid + 1

print(ans)
