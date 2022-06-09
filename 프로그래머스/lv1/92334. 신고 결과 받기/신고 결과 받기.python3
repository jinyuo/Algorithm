def solution(id_list, report, k):
    declare = dict()
    for r in set(report):
        user_id, declare_id = r.split()
        if declare_id not in declare.keys():
            declare[declare_id] = set()
            declare[declare_id].add(user_id)
        else:
            declare[declare_id].add(user_id)

    mail = [0 for _ in range(len(id_list))]
    for val in declare.values():
        if len(val) >= k:
            for v in val:
                mail[id_list.index(v)] += 1
    
    return mail