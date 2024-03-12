def solution(arrayA, arrayB):
    a = arrayA[0]
    b = arrayB[0]

    for i in arrayA[1:]:
        a = gcd(i, a)

    for i in arrayB[1:]:
        b = gcd(i, b)

    return max(find(arrayB, a), find(arrayA, b))


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def find(arr, num):
    for i in range(len(arr)):
        if arr[i] % num == 0:
            return 0
    return num