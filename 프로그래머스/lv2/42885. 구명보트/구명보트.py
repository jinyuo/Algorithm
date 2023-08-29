def solution(people, limit):
    people = sorted(people, reverse=True)

    answer = 0
    start = 0
    end = len(people) - 1
    while start <= end:
        if (people[start] + people[end]) <= limit:
            end -= 1
        start += 1
        answer += 1

    return answer 