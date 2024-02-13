def solution(price, money, count):
    pay = 0

    for i in range(count):
        pay += price * (i + 1)

    if money >= pay:
        return 0
    else:
        return pay - money