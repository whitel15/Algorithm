def solution(food):
    answer = ''
    a = ""

    for i in range(1, len(food)):
        for j in range(food[i] // 2):
            a += str(i)
    answer = a + "0"

    return answer + a[::-1]