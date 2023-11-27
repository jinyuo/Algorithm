def solution(a, b, n):
    answer = 0

    while n >= a:
        re = (n // a) * b
        n = re + n % a
        answer += re

    return answer