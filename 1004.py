case=int(input())
for i in range(case):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    c=0
    for j in range(n):
        X, Y, R = map(int, input().split())
        d1 = ((x1 - X) ** 2 + (y1 - Y) ** 2) ** 0.5
        d2 = ((x2 - X) ** 2 + (y2 - Y) ** 2) ** 0.5

        if(d1<R and d2>R) or (d1>R and d2<R):
            c+=1
    print(c)


