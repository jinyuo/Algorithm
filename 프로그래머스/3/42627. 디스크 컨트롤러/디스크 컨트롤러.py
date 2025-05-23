def solution(jobs):
    jobs = sorted(jobs)
    answer = 0
    queue = []
    cur_time = 0
    idx = 0

    while idx < len(jobs) or queue:
        # 대기 큐
        for i in range(idx, len(jobs)):
            job = jobs[i]
            if cur_time >= job[0]:
                queue.append([job[0], job[1], i])
                idx += 1

        if queue:
            queue = sorted(queue, key=lambda x: (x[1], x[2]))
            task = queue.pop(0)
            answer += cur_time + task[1] - task[0]
            cur_time += task[1] - 1

        cur_time += 1

    return answer // len(jobs)