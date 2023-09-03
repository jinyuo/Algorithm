import math

def solution(n,a,b):
    answer = 0
    while a - 1 != b - 1:
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        answer += 1
    return answer