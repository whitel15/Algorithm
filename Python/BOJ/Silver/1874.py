import sys
input = sys.stdin.readline

N = int(input())
L = [0] * N
stack = []
K = 1
j = 0
pr = []
fa = 0
for i in range(N):
    L[i] = int(input())

while j != N:
    if K > L[j]:
        a = stack.pop()
        if a != L[j]:
            print("NO")
            fa = 1
            break
        pr.append("-")
        j += 1
    elif K <= L[j]:
        stack.append(K)
        pr.append("+")
        K += 1

if fa == 0:
    for k in range(len(pr)):
        print(pr[k])
