from collections import Counter

def solution(s):
    s = list(map(int, s.replace('{', '').replace('}', '').split(',')))
    tple = [c[0] for c in Counter(s).most_common()]
    return tple