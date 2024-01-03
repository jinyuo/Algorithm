from itertools import permutations

def is_prime(n):
    if n <= 1: 
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: 
            return False
    return True


def solution(numbers):
    answer = set()
    
    for i in range(len(numbers)):
        for p in set(permutations(numbers, i + 1)):
            n = int(''.join([s for s in p]))
            if is_prime(n):
                answer.add(n)
    
    return len(answer)