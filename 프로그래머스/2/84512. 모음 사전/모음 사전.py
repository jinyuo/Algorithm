from itertools import product

def solution(word):
    raw = 'AEIOU'
    dictionaries = [''.join(t) for i in range(5) for t in product(raw, repeat=i + 1) ]
    return sorted(dictionaries).index(word) + 1