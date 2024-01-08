import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

answer = [i for i in range(1, 10001)]
SN = [1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97]


def d(n):
    ans = int(n)
    for i in range(len(n)):
        ans += int(n[i])
    return ans


for i in range(1, 10000):
    if d(str(i)) in answer:
        answer.remove(d(str(i)))

for i in answer:
    print(i)