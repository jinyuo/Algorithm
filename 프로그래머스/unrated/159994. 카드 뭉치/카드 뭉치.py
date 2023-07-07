def solution(cards1, cards2, goal):
    answer = 'Yes'
    for g in goal:
        # try:
        if cards1 and g == cards1[0]:
            del cards1[0]
        elif cards2 and g == cards2[0]:
            del cards2[0]
        else:
            answer = 'No'
        # except:
        #     answer = 'No'
    
    return answer