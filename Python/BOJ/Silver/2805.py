import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

s, e = 0, max(tree)
idx = 0

while s <= e:
    mid = (s + e) // 2
    total = 0

    total = sum(tree[i] - mid for i in range(n) if tree[i] > mid)

    if total >= m:
        s = mid + 1
        idx = mid
    else:
        e = mid - 1

print(idx)
