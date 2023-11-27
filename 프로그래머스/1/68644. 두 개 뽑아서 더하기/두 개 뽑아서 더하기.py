from itertools import combinations

def solution(numbers):
    a = set(sum(com) for com in combinations(numbers, 2))
    a = sorted(list(a))
    return a