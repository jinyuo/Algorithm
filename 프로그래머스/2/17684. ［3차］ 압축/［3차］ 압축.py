def solution(msg):
    w = ''
    zip_dict = {i: ord(i) - 64 for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    answer = []
    for c in msg:
        list_keys = zip_dict.keys()
        if w + c in list_keys:
            w = w + c
        else:
            zip_dict[w + c] = len(list_keys) + 1
            answer.append(zip_dict[w])
            w = c
    answer.append(zip_dict[w])
    return answer
