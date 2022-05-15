import sys
n=int(sys.stdin.readline())
a=sorted(map(int,sys.stdin.readline().split()))
d=0
for i in range(n):
  d+=a[i]*(2*i-n+1)
print(d*2)