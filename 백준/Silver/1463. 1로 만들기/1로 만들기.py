def solution(n):
    memo = [0, 0]
    for i in range(2, int(n) + 1):
        cnt = memo[i - 1] + 1
        if i % 3 == 0:
            cnt = min(cnt, memo[i // 3] + 1)
        if i % 2 == 0:
            cnt = min(cnt, memo[i // 2] + 1)
        memo.append(cnt)
    return memo[-1]


n = input()
print(solution(n))