def solution(players, callings):
    map_name_rank = {players[i]: i for i in range(len(players))}
        
    for call in callings:
        lose_run = map_name_rank[call]
        win_run = lose_run - 1
        
        map_name_rank[call] = win_run
        map_name_rank[players[win_run]] = lose_run
        players[win_run], players[lose_run] = players[lose_run], players[win_run]
        
    return players

