from collections import Counter

def solution(k, tangerine):
    t_group = Counter(tangerine)
    t_group = sorted(t_group.items(), key=lambda x: x[1], reverse=True)
    answer = 0
    cnt = 0
    for g, c in t_group:
        if cnt < k:
            cnt += c
            answer += 1
    return answer