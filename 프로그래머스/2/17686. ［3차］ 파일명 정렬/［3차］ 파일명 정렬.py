import re

def solution(files):
    answer = []

    for f in files:
        split = re.match('(?P<head>\D+)(?P<number>\d{1,5})(?P<tail>.*)', f).groupdict()
        split['file'] = f
        split['head'] = split['head'].lower()
        split['number'] = int(split['number'])
        answer.append(split)

    answer = sorted(answer, key=lambda x: (x['head'], x['number']))
    answer = [a['file'] for a in answer]

    return answer