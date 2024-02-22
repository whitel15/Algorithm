def solution(numbers, hand):
    answer = ''
    L = [1, 4, 7]
    R = [3, 6, 9]
    mid = {2: 0, 5: 1, 8: 2, 0: 3}
    lf = [3, 0]
    rf = [3, 2]

    for i in numbers:
        if i in L:
            answer += "L"
            lf = [i // 3, 0]
        elif i in R:
            answer += "R"
            rf = [i // 4, 2]
        else:
            if abs(lf[0] - mid[i]) + abs(lf[1] - 1) < abs(rf[0] - mid[i]) + abs(rf[1] - 1):
                answer += "L"
                lf = [mid[i], 1]
            elif abs(lf[0] - mid[i]) + abs(lf[1] - 1) > abs(rf[0] - mid[i]) + abs(rf[1] - 1):
                answer += "R"
                rf = [mid[i], 1]
            else:
                if hand == "left":
                    answer += "L"
                    lf = [mid[i], 1]
                else:
                    answer += "R"
                    rf = [mid[i], 1]

    return answer