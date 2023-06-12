import heapq

def solution(operations):
    heap = []
    for oper in operations:
        op, val = oper.split()
        if op == 'I':
            heapq.heappush(heap, int(val))
        elif op == 'D':
            try:
                if val == '-1':
                    heapq.heappop(heap)
                else:
                    max_heap = [-1 * h for h in heap]
                    print(max_heap)
                    heapq.heapify(max_heap)
                    heapq.heappop(max_heap)
                    heap = [-1 * h for h in max_heap]
                    heapq.heapify(heap)         
            except:
                pass
    return [max(heap), min(heap)] if heap else [0, 0]