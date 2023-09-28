from collections import Counter

def solution(want, number, discount):
    want_d = dict(zip(want, number))
    
    answer = 0
    for i in range(len(discount) - 9):
        cnt_d = Counter(discount[i:i+10])
        if cnt_d == want_d:
            answer += 1
    
    return answer