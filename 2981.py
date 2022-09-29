import sys
import math
n=int(input())
nl=[]
ans=[]
gcd=0
for i in range(n):
    nl.append(int(sys.stdin.readline().rstrip()))
    if i==1:
        gcd=(abs(nl[1]-nl[0]))
    gcd=math.gcd(abs(nl[i]-nl[i-1]),gcd)
gcd_range=int(gcd**0.5)+1
for i in range(2,gcd_range):
    if gcd%i==0:
        ans.append(i)
        ans.append(gcd//i)
ans.append(gcd)
ans=list(set(ans))
ans.sort()
for i in ans:
    print(i,end=' ')
