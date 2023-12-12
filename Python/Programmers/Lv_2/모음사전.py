from itertools import product

def solution(word):
    dic = set()
    for i in product(["", "A", "E", "I", "O", "U"], repeat = 5):
        dic.add("".join(i))
    dic = sorted(dic)
    for idx, w in enumerate(dic):
        if w == word:
            return idx