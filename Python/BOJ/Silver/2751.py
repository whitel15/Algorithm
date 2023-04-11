import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
A = [0] * (N + 1)
tmp = [0] * (N + 1)
for i in range(N):
    A[i+1] = int(input())


def sort(s, e):
    if e - s < 1:
        return
    m = (e + s) // 2
    sort(s, m)
    sort(m + 1, e)
    for i in range(s, e+1):
        tmp[i] = A[i]
    k = s
    a = s
    b = m + 1
    while a <= m and b <= e:
        if tmp[a] < tmp[b]:
            A[k] = tmp[a]
            k += 1
            a += 1
        elif tmp[a] > tmp[b]:
            A[k] = tmp[b]
            k += 1
            b += 1
    while a <= m:
        A[k] = tmp[a]
        k += 1
        a += 1
    while b <= e:
        A[k] = tmp[b]
        k += 1
        b += 1
    return A

sort(1, N)
for i in range(1, N + 1):
    print(str(A[i]) + '\n')
