def solution(x, y, n):
    memo = [-1 for _ in range(x + 1)]
    memo[x] = 0
    for i in range(x + 1, y + 1):
        cnt = -1
        if i - n >= x and memo[i - n] >= 0:
            cnt = memo[i - n] + 1
        if i % 2 == 0 and memo[i // 2] >= 0:
            cnt = min(memo[i // 2] + 1, cnt) if cnt >= 0 else memo[i // 2] + 1
        if i % 3 == 0 and memo[i // 3] >= 0:
            cnt = min(memo[i // 3] + 1, cnt) if cnt >= 0 else memo[i // 3] + 1
        memo.append(cnt)
    return memo[-1] if memo[-1] >= 0 else -1