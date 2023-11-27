def solution(X, Y):
    xy = {}
    for k in set(str(X)) & set(str(Y)):
        xy[k] = min(str(X).count(k), str(Y).count(k))

    ordered_key = sorted(xy, key=lambda x:x, reverse=True)
    if ordered_key == ['0']:
        answer = '0'
    elif not ordered_key:
        answer = '-1'
    else:
        answer = ''
        for c in ordered_key:
            answer += str(c) * xy[c]
    return answer