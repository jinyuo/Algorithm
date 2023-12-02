def solution(msg):
    zip_dict = {i: ord(i) - 64 for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    answer = []
    while msg:
        list_key = list(zip_dict.keys())[::-1]
        for k in list_key:
            if msg.startswith(k):
                answer.append(zip_dict[k])
                msg = msg.replace(k, '', 1)
                if msg:
                    zip_dict[k + msg[0]] = len(list_key) + 1
                break
    return answer
