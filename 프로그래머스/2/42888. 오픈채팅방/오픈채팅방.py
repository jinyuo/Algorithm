map_action = {
    "Enter": "들어왔습니다.",
    "Leave": "나갔습니다."
}

def solution(record):
    map_uid_nickname = dict()
    for r in record:
        action, uid, *nickname = r.split(" ")
        if action in ['Enter', 'Change']:
            map_uid_nickname[uid] = nickname[0]
    
    result = []
    for r in record:
        action, uid, *nickname = r.split(" ")
        if action in ['Enter', 'Leave']:
            result.append(f"{map_uid_nickname[uid]}님이 {map_action[action]}")
            
    return result