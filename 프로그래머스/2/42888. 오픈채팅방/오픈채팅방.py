def solution(record):
    answer = []

    map_uid_uname = dict()
    for r in record:
        try:
            cmd, uid, uname = r.split()
        except ValueError:
            cmd, uid = r.split()

        if cmd in ('Enter', 'Change'):
            map_uid_uname[uid] = uname

    for r in record:
        try:
            cmd, uid, uname = r.split()
        except ValueError:
            cmd, uid = r.split()

        if cmd == 'Enter':
            answer.append(f'{map_uid_uname[uid]}님이 들어왔습니다.')
        elif cmd == 'Leave':
            answer.append(f'{map_uid_uname[uid]}님이 나갔습니다.')

    return answer