def solution(n, left, right):
    start_row, start_col = (left) // n, (left) % n
    end_row, end_col = (right) // n, (right) % n
    
    answer = []
    for i in range(start_row, end_row + 1):
        tmp = [i + 1 for t in range(n)]
        for j in range(i, n):
            tmp[j] += j - i
        answer += tmp
    answer = answer[start_col:]
    return answer[:right - left + 1]