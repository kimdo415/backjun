n=int(input())
a=list(map(int, input().split()))
s=int(input())

c=0

for i in range(len(a)-1):
    if a[i]<a[i+1]:
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp
        c+=1
        if c==s:
            break
print(' '.join(list(map(str, a))))