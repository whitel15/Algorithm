def solution(arr1, arr2):
    a1 = len(arr1)
    a2 = len(arr2)
    b2 = len(arr2[0])

    answer = [[] for _ in range(a1)]

    for i in range(a1):
        for j in range(b2):
            num = 0
            for z in range(a2):
                num += arr1[i][z] * arr2[z][j]
            answer[i].append(num)

    return answer