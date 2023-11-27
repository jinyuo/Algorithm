def solution(survey, choices):
    mbti = {'RT': 0, 'CF': 0, 'JM': 0, 'AN': 0}
    choice_standard = 4
    for s, c in zip(survey, choices):
        if s in mbti.keys():
            mbti[s] += (choice_standard - c)
        elif s[::-1] in mbti.keys():
            mbti[s[::-1]] -= (choice_standard - c)
        else:
            mbti[s] = choice_standard - c

    answer = ''.join(m[0] if mbti[m] >= 0 else m[-1] for m in mbti.keys())
    return answer