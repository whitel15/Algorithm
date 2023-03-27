import sys
input = sys.stdin.readline

A = int(input())
num = 1
sp = 1
ep = 1
sum = 1

while ep != A:
    if sum == A:
        num += 1
        ep += 1
        sum += ep
    elif sum < A:
        ep += 1
        sum += ep
    elif sum > A:
        sum -= sp
        sp += 1

print(num)