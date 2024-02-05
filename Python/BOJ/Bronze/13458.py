import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
ans = 0

for i in range(n):
    num = a[i] - b
    ans += 1
    if num > 0:
        x = num // c
        if num % c == 0:
            ans += x
        else:
            y = 1
            ans += (x + y)

print(ans)
