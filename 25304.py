r=int(input())
s=0
n=int(input())
for i in range(n):
    x,y=map(int, input().split())
    s += (x*y)
if r==s:
    print('Yes')
else:
    print('No')