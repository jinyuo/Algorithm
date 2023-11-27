def solution(s):
    del_zeros = 0
    cnt = 0
    while s != '1':
        tmp_s = s.replace('0', '')
        del_zeros += len(s) - len(tmp_s)
        s = bin(len(tmp_s))[2:]
        cnt += 1
    
    return [cnt, del_zeros]