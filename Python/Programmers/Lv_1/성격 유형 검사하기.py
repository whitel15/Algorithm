def solution(survey, choices):
    answer = ''

    personality = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for i in range(len(choices)):
        if choices[i] > 4:
            personality[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            personality[survey[i][0]] += 4 - choices[i]

    if personality["T"] > personality["R"]:
        answer += "T"
    else:
        answer += "R"

    if personality["F"] > personality["C"]:
        answer += "F"
    else:
        answer += "C"

    if personality["M"] > personality["J"]:
        answer += "M"
    else:
        answer += "J"

    if personality["N"] > personality["A"]:
        answer += "N"
    else:
        answer += "A"

    return answer