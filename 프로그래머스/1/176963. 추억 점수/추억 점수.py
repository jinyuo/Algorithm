def solution(name, yearning, photo):
    score = {name[i]: yearning[i] for i in range(len(name))}
    
    answer = []
    for ph in photo:
        answer.append(sum([score[p] for p in ph if p in score.keys()]))
    return answer