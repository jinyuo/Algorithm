from collections import Counter

def solution(N, stages):
    clear_players = len(stages)
    not_cleared = Counter(stages)
    ratios = []
    
    for i in range(1, N + 1):
        players = not_cleared.get(i, 0)
        ratios.append([i, (players / clear_players) if players != 0 else 0])
        clear_players -= players
    
    ratios.sort(key=lambda x: (-x[1], x[0]))

    return [ratio[0] for ratio in ratios]