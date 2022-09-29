from collections import deque

n,k=map(int,input().split())
n=deque(range(1,n+1))

i=1
re=[]
while n:
    if i%k==0:
        re.append(n.popleft())
    else:
        n.append(n.popleft())
    i +=1
print("<"+", ".join(map(str,re))+">")