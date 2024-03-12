op = list()
for i in range(0, 3):
    op.append(input())
print(int(op[0]) + int(op[2]) if op[1] == '+' else int(op[0]) * int(op[2]))