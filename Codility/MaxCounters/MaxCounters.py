def solution(N, A):
    # Implement your solution here
    d = dict()
    max_counter = 0
    for a in A:
        if a >= 1 and a <= N:
            if a not in d.keys():
                d[a] = 1
            else:
                d[a] += 1
        elif a == N + 1:
            if d:
                max_counter += max(v for v in d.values())
                d = dict()

    result = [max_counter for i in range(N)]
    for k, v in d.items():
        result[k - 1] += v
    return result
