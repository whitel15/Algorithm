import sys
input = sys.stdin.readline

n = int(input())
budget = list(map(int, input().split()))
m = int(input())

low, high = 0, max(budget)
answer = 0
while low <= high:
    total = 0
    mid = (low + high) // 2

    for num in budget:
        total += min(num, mid)

    if total <= m:
        low = mid + 1
        answer = mid
    else:
        high = mid - 1

print(answer)