n,m=map(int, input().split())
ans=[]
for i in range(n):
    ans.append(list(map(int, input().split())))

c=int(input())
for i in range(c):
    x1,y1,x2,y2=map(int, input().split())
    sum=0
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            sum = sum+ans[i][j]
    print(sum)