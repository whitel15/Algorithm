def solution(genres, plays):
    answer = []
    index = 0
    dic = {}
    dic2 = {}

    # key - genres, value - (plays, index) 인 dic 생성
    for i, j in zip(genres, plays):
        if i in dic:
            dic[i].append((j, index))
            index += 1
        else:
            dic[i] = []
            dic[i].append((j, index))
            index += 1

    # 각 key의 value를 plays를 내림차순 정렬한 값으로 정렬
    for key, value in dic.items():
        dic[key] = sorted(value, key=lambda x: x[0], reverse=True)
        # plays의 합을 value로 갖는 dic2 생성
        dic2[key] = sum(play for play, _ in value)

    # dic2를 value의 내림차순으로 정렬한 sorted_dic2 생성
    sorted_dic2 = dict(sorted(dic2.items(), key=lambda item: item[1], reverse=True))

    # 속한 노래가 많이 재생된 장르 순, 장르 내에서 많이 재생된 노래를 먼저, 재생 횟수가 같다면 고유 번호 순으로 수록
    for i in sorted_dic2:
        if len(dic[i]) == 1:
            answer.append(dic[i][0][1])
        else:
            answer.append(dic[i][0][1])
            answer.append(dic[i][1][1])

    return answer
