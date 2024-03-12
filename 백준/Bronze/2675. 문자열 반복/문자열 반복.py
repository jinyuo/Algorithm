loop = int(input())
for i in range(loop):
    tmp = ""
    info = input().split()
    for j in range(len(info[1])):
        tmp += info[1][j] * int(info[0])
    print(tmp)