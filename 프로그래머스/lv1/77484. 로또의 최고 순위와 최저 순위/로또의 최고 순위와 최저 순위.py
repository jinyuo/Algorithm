def solution(lottos, win_nums):
    lottos = set(lottos)
    lottos.discard(0)
    win_nums.sort()
    cnt = 0
    g = [6,6,5,4,3,2,1]
    for l in lottos:
        if l in win_nums:
            cnt += 1
            
    return [g[cnt + 6 - len(lottos)], g[cnt]]