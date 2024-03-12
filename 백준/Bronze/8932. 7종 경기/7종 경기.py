import sys
score = {0: [9.23076, 26.7, 1.835, 'sec', '트랙'], 1: [1.84523, 75, 1.348, 'cm', '필드'],
         2: [56.0211, 1.5, 1.05, 'm', '필드'], 3: [4.99087, 42.5, 1.81, 'sec', '트랙'],
         4: [0.188807, 210, 1.41, 'cm', '필드'], 5: [15.9803, 3.8, 1.04, 'm', '필드'], 6: [0.11193, 254, 1.88, 'sec', '트랙']}

t = int(sys.stdin.readline())
for _ in range(t):
    li = list(map(int, sys.stdin.readline().split()))
    s = 0
    for i in range(len(li)):
        if score[i][4] == "필드":
            s += int(score[i][0] * (li[i] - score[i][1]) ** score[i][2])
        else:
            s += int(score[i][0] * (score[i][1] - li[i]) ** score[i][2])
    print(s)
