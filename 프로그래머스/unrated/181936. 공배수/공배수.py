def solution(number, n, m):
    if number % n == number % m == 0:
        return 1
    else:
        return 0
    