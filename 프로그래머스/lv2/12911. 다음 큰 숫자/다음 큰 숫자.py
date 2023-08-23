def solution(n):
    bin_n = '0' + bin(n)[2:]
    idx_one = bin_n.rfind('1')
    idx_zero = bin_n.rfind('0', 0, idx_one)
    cnt_zero = len(bin_n) - idx_one - 1
    cnt_one = idx_one - idx_zero - 1
    answer = bin_n[:idx_zero] + bin_n[idx_zero:idx_zero + 2][::-1] + '0' * cnt_zero + '1' * cnt_one
    
    return int(answer, base=2)