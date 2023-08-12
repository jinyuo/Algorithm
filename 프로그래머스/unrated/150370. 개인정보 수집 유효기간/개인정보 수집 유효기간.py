from datetime import datetime
def solution(today, terms, privacies):
    today = datetime.strptime(today, '%Y.%m.%d')
    map_term = dict()
    for t in terms:
        tp, period = t.split()
        map_term[tp] = int(period)
    
    answer = []
    for i, p in enumerate(privacies):
        start_date, ty = p.split()
        start_date = datetime.strptime(start_date, '%Y.%m.%d')
        add_month = start_date.month + map_term[ty] - 1
        year = start_date.year + int(add_month / 12)
        month = add_month % 12 + 1
        end_date = datetime(year, month, start_date.day)
        if today >= end_date:
            answer.append(i + 1)
    return answer