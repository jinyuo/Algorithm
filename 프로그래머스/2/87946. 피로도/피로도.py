from itertools import permutations

def game(k, dungeons):
    cnt = 0
    for require, consume in dungeons:
        if k < require:
            return cnt
        k -= consume
        cnt += 1
    return cnt
    
def solution(k, dungeons):
    return max([game(k, permutation) for permutation in permutations(dungeons, len(dungeons))])
