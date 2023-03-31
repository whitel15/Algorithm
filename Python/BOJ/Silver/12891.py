import sys
input = sys.stdin.readline

S, P = map(int, input().split())
string = list(input())

a, c, g, t = map(int, input().split())

result = 0

start = string[:P]

tmp = {"A": 0, "C": 0, "G": 0, "T": 0}

for i in range(P):
    tmp[string[i]] += 1

if tmp['A'] >= a and tmp['C'] >= c and tmp['G'] >= g and tmp['T'] >= t:
    result += 1

for i in range(S-P):
    tmp[string[i]] -= 1
    tmp[string[P+i]] += 1
    if tmp['A'] >= a and tmp['C'] >= c and tmp['G'] >= g and tmp['T'] >= t:
        result += 1

print(result)