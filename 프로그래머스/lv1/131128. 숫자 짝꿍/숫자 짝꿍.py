def solution(X, Y):
    xy = {}
    for k in set(str(X)) & set(str(Y)):
        xy[k] = min(str(X).count(k), str(Y).count(k))

    ordered_key = sorted(xy, key=lambda x:x, reverse=True)
    answer = ''
    for c in ordered_key:
        answer += str(c) * xy[c]
    
    if all([k == '0' for k in ordered_key]):
        answer = '0'
    if not ordered_key:
        answer = '-1'
    return answer