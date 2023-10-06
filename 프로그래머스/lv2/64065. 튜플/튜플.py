def solution(s):
    s = list(map(int, s.replace('{', '').replace('}', '').split(',')))
    answer = sorted(list(set(s)), key=lambda x: s.count(x), reverse=True)
    return answer