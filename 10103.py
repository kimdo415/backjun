case=int(input())
x,y=100,100
for i in range(case):
    n1,n2=map(int, input().split())
    if n1>n2:
        y -= n1
    if n1<n2:
        x -= n2
    else:
        pass
print(x)
print(y)
