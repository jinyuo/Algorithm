import inspect

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''        
    # 분:초를 초로 변환
    list_conv = []
    for var in [video_len, pos, op_start, op_end]:
        minute, sec = map(int, var.split(':'))
        list_conv.append(minute * 60 + sec)

    # 입력 기능
    for command in commands:
        # 오프닝 건너뛰기
        if list_conv[2] <= list_conv[1] < list_conv[3]:
            list_conv[1] = max(list_conv[1], list_conv[3])
    
        if command == 'prev':
            list_conv[1] = max(0, list_conv[1] - 10)
        elif command == 'next':
            list_conv[1] = min(list_conv[1] + 10, list_conv[0])    
    
    # 오프닝 건너뛰기
    if list_conv[2] <= list_conv[1] < list_conv[3]:
        list_conv[1] = max(list_conv[1], list_conv[3])
        
    # 초를 분:초로 변환
    minute, second = divmod(list_conv[1], 60)        
    return f"{minute:02d}:{second:02d}"