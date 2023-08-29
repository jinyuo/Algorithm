def solution(people, limit):
    people = sorted(people, reverse=True)

    answer = 0
    start = 0
    end = len(people) - 1
    while start <= end:
        if (people[start] + people[end]) <= limit:
            start += 1
            end -= 1
        else:
            start += 1
        answer += 1

    return answer