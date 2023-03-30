import sys
input = sys.stdin.readline

N = int(input())
mylist = list(map(int, input().split()))
mylist.sort()
count = 0

for k in range(N):
    target = mylist[k]
    sp = 0
    ep = N - 1
    while sp < ep:
        if mylist[sp] + mylist[ep] == target:
            if sp != k and ep != k:
                count += 1
                break
            elif sp == k:
                sp += 1
            elif ep == k:
                ep -= 1
        elif mylist[sp] + mylist[ep] < target:
            sp += 1
        elif mylist[sp] + mylist[ep] > target:
            ep -= 1

print(count)