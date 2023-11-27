def solution(price, money, count):
    total_price = int(count * (count + 1) * price / 2)
    gap = total_price - money
    if gap < 0:
        gap = 0
    
    return gap