def solution(elements):
    answer = []
    elements += elements

    for s in range(len(elements)//2):
        for l in range(1, len(elements)//2 + 1):
            answer.append(sum(elements[s:s + l]))

    return len(set(answer))