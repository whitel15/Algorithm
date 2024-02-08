from collections import Counter

def solution(want, number, discount):
    answer = 0
    JHL = {}
    for j in range(len(want)):
        JHL[want[j]] = number[j]
    
    for i in range(0, len(discount) - 9):
        if JHL == Counter(discount[i:i+10]):
            answer += 1

    return answer