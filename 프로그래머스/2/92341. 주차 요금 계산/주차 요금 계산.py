from datetime import datetime
import math

def solution(fees, records):
    parking = dict()
    end_time = datetime.strptime('23:59', '%H:%M')
    
    # 주차
    for r in records:
        time, id, state = r.split()
        time = datetime.strptime(time, '%H:%M')
        if state == 'IN':
            save = parking[id][2] if id in parking.keys() else 0
        else:
            save = parking[id][2] + (time - parking[id][1]).seconds / 60
        parking[id] = [state, time, save]
        
    for k, v in parking.items():
        if v[0] == 'IN':
            save = v[2] + (end_time - v[1]).seconds / 60
            parking[k] = ['OUT', end_time, save]
            
    answer = []
    for k in sorted(parking):
        data = parking[k]
        if data[2] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((data[2] - fees[0]) / fees[2]) * fees[3])
            
    return answer