def solution(arr):
    answer = []

    a = min(arr)
    arr.remove(a)
    if len(arr) == 0:
        answer.append(-1)
    else:
        answer = arr

    return answer