def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        line = ""
        num1 = str(bin(arr1[i])[2:]).rjust(n, "0")
        num2 = str(bin(arr2[i])[2:]).rjust(n, "0")
        for j in range(n):
            if int(num1[j]) + int(num2[j]):
                line += "#"
            else:
                line += " "
        answer.append(line)

    return answer