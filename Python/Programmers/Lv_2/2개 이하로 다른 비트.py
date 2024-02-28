
def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            number = "0" + bin(number)[2:]
            for i in range(len(number)):
                idx = len(number) - i - 1

                if number[idx] == "0":
                    answer.append(int(number[:idx] + "10" + number[idx + 2:], 2))
                    break

    return answer