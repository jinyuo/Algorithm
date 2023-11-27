import math

def get_divisor_cnt(n):
    divisor_cnt = 0
    sqrt_n = n ** 0.5
    for i in range(1, math.ceil(sqrt_n)):
        if n % i == 0:
            divisor_cnt += 1
    divisor_cnt = divisor_cnt * 2 + (1 if sqrt_n.is_integer() else 0)
    return divisor_cnt


def solution(number, limit, power):
    answer = 0
    list_power = [get_divisor_cnt(i) for i in range(1, number + 1)]
    list_power = [p for p in list_power if p <= limit] + [power for p in list_power if p > limit]
    return sum(list_power)