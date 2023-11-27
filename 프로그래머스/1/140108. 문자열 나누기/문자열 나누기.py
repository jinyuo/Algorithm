def solution(s):
    answer = 0
    x_cnt, o_cnt = 0, 0
    x = ''
    s = list(s)
    while s:
        tmp = s.pop(0)
        if x == '':
            x = tmp
            x_cnt += 1
        else:
            if x == tmp:
                x_cnt += 1
            else:
                o_cnt += 1
        print(x, tmp)
        if x_cnt == o_cnt:
            answer += 1
            x = ''
    if x_cnt != o_cnt:
        answer += 1
            
    return answer