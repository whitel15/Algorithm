def solution(arr):
    answer = 1
    chk = 1

    while chk:
        arr.sort()
        chk = 0
        for i in range(2, max(arr) + 1):
            a = 0
            for j in range(len(arr)):
                if arr[j] % i == 0:
                    a = 1
                    chk = 1
                    arr[j] = arr[j] // i
            if a:
                answer *= i
                break

    for i in arr:
        answer *= i

    return answer