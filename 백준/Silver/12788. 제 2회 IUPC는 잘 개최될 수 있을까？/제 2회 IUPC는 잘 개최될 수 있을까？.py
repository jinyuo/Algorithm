def check(A, participants):
    total_cnt_pen = 0
    for idx, cnt_pen in enumerate(A):
        total_cnt_pen += cnt_pen
        if total_cnt_pen >= participants:
            return idx + 1

    return 'STRESS'


N = int(input().strip())
M, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
participants = M * K
print(check(A, participants))