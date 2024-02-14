def solution(record):
    answer = []
    nick = {}

    for i in range(len(record)):
        r = record[i].split(" ")
        if r[0] == "Enter" or r[0] == "Change":
            nick[r[1]] = r[2]

    for i in range(len(record)):
        r = record[i].split(" ")
        if r[0] == "Enter":
            answer.append(nick[r[1]] + "님이 들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(nick[r[1]] + "님이 나갔습니다.")

    return answer