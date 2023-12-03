from itertools import permutations

def solution(word):
    raw = 'AEIOU' * 5
    dictionaries = []
    for i in range(1, 6):
        dictionaries += set(''.join(t) for t in permutations(raw, i))
    dictionaries = sorted(dictionaries)

    return dictionaries.index(word) + 1