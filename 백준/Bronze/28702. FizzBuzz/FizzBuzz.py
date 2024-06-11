import sys

list_input = [sys.stdin.readline().strip() for _ in range(3)]
val = [int(v) + (3 - i) for i, v in enumerate(list_input) if v.isnumeric()][0]

answer = ""
if val % 3 == 0:
    answer += 'Fizz'
if val % 5 == 0:
    answer += 'Buzz'
print(answer if answer != '' else val)