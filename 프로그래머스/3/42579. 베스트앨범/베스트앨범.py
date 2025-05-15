def solution(genres, plays):
    list_data = []
    for i, data in enumerate(zip(genres, plays)):
        list_data.append([i, data[0], data[1]])
    
    map_total_plays = dict()
    for i, genre, play in list_data:
        if genre not in map_total_plays.keys():
            map_total_plays[genre] = play
        else:
            map_total_plays[genre] += play
    
    list_data.sort(key=lambda x: (-map_total_plays[x[1]], -x[2], x[0]))
    
    result = []
    for genre, play in sorted(map_total_plays.items(), key=lambda x: -x[1]):
        d = [i for i, r, p in list_data if r == genre]
        result.extend(d[:min(2, len(d))])
        
    return result