import string

def convert(n, k):
    tmp = string.digits + string.ascii_uppercase
    q, r = divmod(n, k)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, k) + tmp[r]


def solution(n, t, m, p):
    answer = ''
    str_num = ''
    num = 0
    while len(str_num) < m * t + p:
        str_num += convert(num, n)
        num += 1
    
    return str_num[p-1::m][:t]