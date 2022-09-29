a,b= map(int, input().split())
ans=[0]
for i in range(46):
    for j in range(i):
        ans.append(i)
print(sum(arr[a:b+1]))