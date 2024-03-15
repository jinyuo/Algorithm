import sys

while True:
    num = sys.stdin.readline().strip()
    if num == '0':
        exit()
    print('yes' if num == num[::-1] else 'no')
