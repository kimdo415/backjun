t=int(input())

m1,m2,s=0,0,0

if t%10!=0:
    print(-1)
else:
    m1=t//300
    m2=(t%300)//60
    s=(t%300)%60//10
    print(m1,m2,s)
