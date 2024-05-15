def solution(storey):
    answer = 0
    loop = storey
    while loop > 0:
        print(loop)
        r = loop % 10
        if r == 0:
            while loop % 10 == 0:
                loop //= 10
        elif r < 5:
            answer += r
            loop = loop // 10
        elif r == 5:
            if (loop // 10) % 10 >= 5:
                r = 10 - r
                answer += r
                loop = (loop + r) // 10
            else :
                answer += r
                loop = loop // 10
                
        else:
            r = 10 - r
            answer += r
            loop = (loop + r) // 10
    return answer