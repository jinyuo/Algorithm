import heapq

def solution(k, score):
    answer = [min(heapq.nlargest(min(i, k), score[:i])) for i in range(1, len(score) + 1)]
    return answer