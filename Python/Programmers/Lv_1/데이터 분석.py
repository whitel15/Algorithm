def solution(data, ext, val_ext, sort_by):
    answer = []
    idx = 0
    Sidx = 0

    db = ["code", "date", "maximum", "remain"]

    idx = db.index(ext)
    Sidx = db.index(sort_by)

    for i in range(len(data)):
        if data[i][idx] < val_ext:
            answer.append(data[i])

    answer.sort(key=lambda x: x[Sidx])

    return answer