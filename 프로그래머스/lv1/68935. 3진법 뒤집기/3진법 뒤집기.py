def solution(n):
    sam = ''
    while n != 0:
        n, reminder = divmod(n, 3)
        sam += str(reminder)
        
    return int(sam, 3)