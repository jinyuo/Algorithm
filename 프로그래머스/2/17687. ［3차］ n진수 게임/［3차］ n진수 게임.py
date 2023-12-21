import string


def num_base_convert(num, base):
    tmp = string.digits + string.ascii_uppercase
    result = ''
    while num // base > 0:
        num, r = divmod(num, base)
        result = tmp[r] + result

    return tmp[num] + result


def solution(n, t, m, p):
    answer = ''
    str_num = ''
    num = 0
    while len(str_num) < m * t + p:
        str_num += num_base_convert(num, n)
        num += 1
    
    return str_num[p-1::m][:t]