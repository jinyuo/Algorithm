import string

def convert(n, k):
    tmp = string.digits + string.ascii_lowercase
    q, r = divmod(n, k)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, k) + tmp[r]

    
def isprime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True
    
    
def solution(n, k):
    answer = 0
    list_num = [int(n) for n in convert(n, k).split('0') if n != '' and n != '1']

    for n in list_num:
        if isprime(n):
            answer += 1

    return answer