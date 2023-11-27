def solution(players, callings):
    map_name_rank = {players[i]: i for i in range(len(players))}
        
    for call in callings:
        passing_rank = map_name_rank[call]
        passed_rank = passing_rank - 1
        
        map_name_rank[call] = passed_rank
        map_name_rank[players[passed_rank]] = passing_rank
        players[passed_rank], players[passing_rank] = players[passing_rank], players[passed_rank]
        
    return players

