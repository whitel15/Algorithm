def solution(s):
    answer = ''
    num = list(s.split(" "))
    findM = []
    for i in range(len(num)):
        findM.append(int(num[i]))
    answer = str(min(findM)) + " " + str(max(findM))
    return answer