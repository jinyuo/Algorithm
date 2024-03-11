import sys


def get_box(size):
    box = []
    for i in range(size):
        if i == 0 or i == size - 1:
            box.append('#' * size)
        else:
            box.append('#' + 'J' * (size - 2) + '#')
    return box


cnt_test_case = int(sys.stdin.readline())
for i in range(cnt_test_case):
    size = int(sys.stdin.readline())
    box = get_box(size)
    print("\n".join(box) + "\n")
