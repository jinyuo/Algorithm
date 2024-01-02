def solution(numbers):
    if all([num == 0 for num in numbers]):
        return '0'
    
    numbers = sorted(numbers, key=lambda x: str(x) * 3, reverse=True)
    return ''.join([str(num) for num in numbers])
    