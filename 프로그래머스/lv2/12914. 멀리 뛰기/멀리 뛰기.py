import math

def solution(n):
    answer = 1
    twos = n // 2
    ones = 0 if n % 2 == 0 else 1

    while twos > 0:
        if ones == 0:
            answer += 1
        else:
            answer += math.factorial(twos + ones) // (math.factorial(twos) * math.factorial(ones))
        twos -= 1
        ones += 2
        answer %= 1234567
    return answer