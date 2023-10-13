from itertools import permutations

def game(k, dungeons):
    cnt = 0
    for dungeon in dungeons:
        if k < dungeon[0]:
            return cnt
        k -= dungeon[1]
        cnt += 1
    return cnt
    
def solution(k, dungeons):
    return max([game(k, permutation) for permutation in permutations(dungeons, len(dungeons))])
