import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))

s = sum(temp[:k])
ans = [s]

for i in range(n-k):
    s += temp[i+k] - temp[i]
    ans.append(s)

print(max(ans))