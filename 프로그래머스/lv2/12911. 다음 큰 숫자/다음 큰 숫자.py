def solution(n):
    bin_n = '0' + bin(n)[2:]
    idx_swap = bin_n.rfind('01')
    cnt_zero = bin_n[idx_swap + 2:].count('0')
    cnt_one = bin_n[idx_swap + 2:].count('1')
    answer = bin_n[:idx_swap] + bin_n[idx_swap:idx_swap + 2][::-1] + '0' * cnt_zero + '1' * cnt_one
    
    return int(answer, base=2)