def solution(babbling):
    defi = ["aya", "ye", "woo", "ma"]
    answer = 0
    for b in babbling:
        pre = ''
        while b != '':
            if pre != defi[0] and b.startswith(defi[0]):
                pre = defi[0]
                b = b[len(defi[0]):]
            elif pre != defi[1] and b.startswith(defi[1]):
                pre = defi[1]
                b = b[len(defi[1]):]
            elif pre != defi[2] and b.startswith(defi[2]):
                pre = defi[2]
                b = b[len(defi[2]):]
            elif pre != defi[3] and b.startswith(defi[3]):
                pre = defi[3]
                b = b[len(defi[3]):]
            else:
                break

        if not b:
            answer += 1
    
    return answer