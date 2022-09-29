ans=[]
num=int(input())

for i in range(num):
    n=int(input())
    ans.append(n)

ans.sort()
for i in ans:
    print(i)
