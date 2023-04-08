import sys
input = sys.stdin.readline
print = sys.stdout.write

s = list(input())
del s[len(s)-1]
max = 0
k = 0
for i in range(len(s)):
    for j in range(len(s)-i):
        if int(s[j]) > max:
            max = int(s[j])
            k = j
    if i != len(s)-1:
        s[k] = s[len(s) - 1 - i]
        s[len(s) - 1 - i] = max
        print(str(max))
        max = 0
    else:
        print(str(max))
        break