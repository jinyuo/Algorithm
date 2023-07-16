from itertools import combinations


def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:           
            for j in range(i+i, n, i): 
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i]]


def solution(nums):
    answer = -1
    list_sum = [sum(combi) for combi in combinations(nums, 3)]
    list_prime = prime_list(max(list_sum) + 1)    
    return len([s for s in list_sum if s in list_prime])