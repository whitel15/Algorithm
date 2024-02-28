import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visiter = list(map(int, input().split()))

s, e = 0, x - 1
max = 0
cnt = 0
ps = sum(visiter[s:e+1])
for i in range(n-x+1):
    x = s + i
    y = e + i
    if i != 0:
        ps = ps - visiter[x-1] + visiter[y]
    if ps > max:
        max = ps
        cnt = 1
    elif ps == max:
        cnt += 1
if max == 0:
    print("SAD")
else:
    print(max)
    print(cnt)