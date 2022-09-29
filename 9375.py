import collections
t=int(input())
for i in range(t):
    a=int(input())
    s=[]
    for j in range(a):
        c,p=input().split()
        s.append(p)
    n=1
    ans=collections.Counter(s)
    for k in ans:
        n *=ans[k]+1
    print(n-1)