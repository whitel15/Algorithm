import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
mylist = list(map(int, input().split()))
mylist.sort()
count = 0
sp = 0
ep = N-1

while sp < ep:
    sum = mylist[sp] + mylist[ep]
    if sum == M:
        count += 1
        sp += 1
        ep -= 1
    elif sum > M:
        ep -= 1
    elif sum < M:
        sp += 1

print(count)