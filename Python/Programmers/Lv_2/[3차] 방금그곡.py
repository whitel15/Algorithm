def solution(m, musicinfos):
    ans = []

    m = m.replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace('G#', 'L')

    for i in musicinfos:
        start, end, name, sheet = i.split(",")
        s = int(start[:2]) * 60 + int(start[3:])
        e = int(end[:2]) * 60 + int(end[3:])
        time = e - s
        sheet = sheet.replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace('G#', 'L')

        if len(sheet) < time:
            sheet += sheet * (time // len(sheet)) + sheet[:(time % len(sheet))]
        elif len(sheet) > time:
            sheet = sheet[:time]

        if m in sheet:
            if len(ans) == 0:
                ans = [time, name]
            else:
                if ans[0] < time:
                    ans = [time, name]

    if len(ans) > 0:
        return ans[1]
    else:
        return "(None)"