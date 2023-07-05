import math

def solution(left, right):
    answer = (right ** 2 - left ** 2 + right + left) // 2
    tmp_sum = 0
    for i in range(math.ceil(left ** 0.5), int(right ** 0.5) + 1):
        tmp_sum += i ** 2
        
    if left == right:
        tmp_sum = left
    
    return answer - 2 * tmp_sum 