import math


def solution(fees, records):
    answer = []
    rec = {}
    sort_car = []

    for i in range(len(records)):
        time, car, state = records[i].split(" ")
        if car in rec:
            rec[car] += [time]
        else:
            rec[car] = [time]

    for key, values in rec.items():
        time = 0

        for i in range(0, len(values) - 1, 2):
            x, y = values[i + 1].split(":")
            OUT = int(x) * 60 + int(y)
            x, y = values[i].split(":")
            IN = int(x) * 60 + int(y)
            time += OUT - IN

        if len(values) % 2 != 0:
            x, y = values[-1].split(":")
            time += 23 * 60 + 59 - int(x) * 60 - int(y)

        if time > fees[0]:
            pay = fees[1] + math.ceil(((time - fees[0]) / fees[2])) * fees[3]
        else:
            pay = fees[1]
        sort_car.append((key, pay))

    sort_car.sort()
    for i in range(len(sort_car)):
        answer.append(sort_car[i][1])

    return answer