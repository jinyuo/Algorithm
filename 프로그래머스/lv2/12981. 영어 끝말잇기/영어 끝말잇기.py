def solution(n, words):
    tmp = []
    answer = [0, 0]
    for i, w in enumerate(words):
        if w in tmp:
            answer = [i % n + 1, i // n + 1]
            return answer
        if tmp and w[0] != tmp[-1][-1]:
            answer = [i % n + 1, i // n + 1]
            return answer          
        tmp.append(w)
    return answer