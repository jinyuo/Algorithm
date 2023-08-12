from datetime import datetime
from dateutil.relativedelta import relativedelta 

def solution(today, terms, privacies):
    today = datetime.strptime(today, '%Y.%m.%d')
    map_term = dict()
    for t in terms:
        tp, period = t.split()
        map_term[tp] = int(period)
    
    answer = []
    for i, p in enumerate(privacies):
        start_date, tp = p.split()       
        end_date = datetime.strptime(start_date, '%Y.%m.%d') + relativedelta(months=map_term[tp])
        if today >= end_date:
            answer.append(i + 1)
    return answer