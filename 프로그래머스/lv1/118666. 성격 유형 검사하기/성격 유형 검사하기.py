def solution(survey, choices):
    mbti = dict()
    metrics = ['RT', 'CF', 'JM', 'AN']
    choice_standard = 4
    for s, c in zip(survey, choices):
        if s in mbti.keys():
            mbti[s] += (choice_standard - c)
        else:
            mbti[s] = choice_standard - c
    
    tmp_mbti = dict()
    for m in metrics:
        tmp_mbti[m] = mbti.get(m, 0) - mbti.get(m[::-1], 0)
    
    answer = ''.join(m[0] if tmp_mbti[m] >= 0 else m[-1] for m in tmp_mbti.keys())
    return answer