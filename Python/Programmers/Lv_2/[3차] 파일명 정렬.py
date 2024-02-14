def solution(files):
    answer = []
    num = [str(i) for i in range(10)]
    nFile = []

    for i in range(len(files)):
        for j in range(len(files[i])):
            if files[i][j] in num:
                a = 0
                while True:
                    a += 1
                    if j + a >= len(files[i]) or files[i][j + a] not in num:
                        break
                h = files[i][:j]
                n = files[i][j:j + a]
                t = files[i][j + a:]
                nFile.append([h, n, t])
                break

    nFile.sort(key=lambda x: (x[0].upper(), int(x[1])))

    for i in range(len(nFile)):
        line = nFile[i][0] + nFile[i][1] + nFile[i][2]
        answer.append(line)

    return answer