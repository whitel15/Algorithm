def solution(s):
    answer = True
    a = 0
    b = 0

    for i in s:
        if i == "p" or i == "P":
            a += 1
        elif i == "y" or i == "Y":
            b += 1

    if a != b:
        return False

    return True