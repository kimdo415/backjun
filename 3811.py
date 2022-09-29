a,b=map(int, input().split())
x = list(map(int, input().split(',')))


for i in range(b):
    ans=[]
    for j in range(len(x)-1):
        ans.append(x[j+1]-x[j])
    x=ans
print(','.join(map(str,x)))