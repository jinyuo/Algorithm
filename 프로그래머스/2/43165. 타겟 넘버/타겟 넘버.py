from itertools import product

def solution(numbers, target):
    len_num = len(numbers)
    list_oper = [p for p in product([1, -1], repeat=len_num)]
    list_sum = [sum([oper[i] * numbers[i] for i in range(len_num)]) for oper in list_oper]

    return list_sum.count(target)
