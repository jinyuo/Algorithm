from collections import Counter

def solution(k, tangerine):
    t_group = Counter(tangerine)
    answer = 0
    cnt = 0
    for key, c in t_group.most_common():
        if cnt < k:
            cnt += c
            answer += 1
    return answer