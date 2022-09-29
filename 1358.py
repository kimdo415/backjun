W,H,X,Y,P=map(int, input().split())
ans=0
for i in range(P):
    x1,y1=map(int, input().split())

    r=H//2
    d1=((X-x1)**2+((y1-(Y+r))**2))**0.5
    d2 =(((X+W) - x1) ** 2 + ((y1 - (Y + r)) ** 2)) ** 0.5

    if (d1<=r or d2<=r) or ((X<=x1<=X+W) and (Y<=y1<=Y+H)):
        ans +=1
print(ans)