def solution(today, terms, privacies):
    answer = []
    term = {}
    idx = 1

    for i in terms:
        a, b = i.split(" ")
        term[a] = int(b)

    for privacy in privacies:
        date, opt = privacy.split(" ")
        year = int(date[:4])
        month = int(date[5:7])
        day = date[8:]

        if month + term[opt] > 12:

            a = term[opt] // 12
            year += a
            left = term[opt] - 12 * a

            if month + left > 12:
                year += 1
                month = str(month + left - 12)
            else:
                month = str(month + left)
        else:
            month = str(month + term[opt])

        if len(month) < 2:
            month = "0" + month

        if today >= str(year) + "." + month + "." + day:
            answer.append(idx)
        idx += 1

    return answer