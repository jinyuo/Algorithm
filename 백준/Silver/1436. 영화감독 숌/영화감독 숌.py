import sys

N = int(sys.stdin.readline())
list_series = []
series_num = 666
while len(list_series) < N:
    if str(series_num).__contains__('666'):
        list_series.append(series_num)
    series_num += 1
print(list_series[-1])