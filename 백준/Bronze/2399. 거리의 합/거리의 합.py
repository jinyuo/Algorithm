n=int(input())
a=sorted(map(int,input().split()))
d=0
for i in range(n):
  d+=a[i]*(2*i-n+1)
print(d*2)