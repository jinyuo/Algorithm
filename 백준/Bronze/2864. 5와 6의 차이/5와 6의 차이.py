import sys
a, b = sys.stdin.readline().split()
a_list = [int(a)]
b_list = [int(b)]
if a.find('5') > -1:
    a_list.append(int(a.replace('5', '6')))
if a.find('6') > -1:
    a_list.append(int(a.replace('6', '5')))
if b.find('5') > -1:
    b_list.append(int(b.replace('5', '6')))
if b.find('6') > -1:
    b_list.append(int(b.replace('6', '5')))
print(min(a_list) + min(b_list), max(a_list) + max(b_list))