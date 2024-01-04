def hanoi(n, from_p, to_p, aux_p, step): # 매개변수 n은 원반 수, from_p는 출발 기둥, to_p는 도착 기둥, aux_p는 보조 기둥
    if n == 1:
        step.append([from_p, to_p])
        return
    hanoi(n - 1, from_p, aux_p, to_p, step) # 보조 기둥으로 이동
    step.append([from_p, to_p])
    hanoi(n - 1, aux_p, to_p, from_p, step) # 도착 기둥으로 이동

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer