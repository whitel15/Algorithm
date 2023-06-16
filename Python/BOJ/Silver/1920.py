N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
Data2 = list(map(int, input().split()))


for i in Data2:
    s = 0
    e = N - 1
    c = 0
    while s <= e:
        pivot = s + (e - s) // 2
        if i == A[pivot]:
            c = 1
            break
        elif i < A[pivot]:
            e = pivot - 1
        elif i > A[pivot]:
            s = pivot + 1
    if c == 1:
        print(1)
    else:
        print(0)
