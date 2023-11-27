import heapq

def solution(scoville, K):
    h = []
    for s in scoville:
        heapq.heappush(h, s)
        
    answer = 0
    while h[0] < K:
        try:
            s = heapq.heappop(h) + heapq.heappop(h) * 2
        except:
            return -1
        heapq.heappush(h, s)
        answer += 1
        
    return answer