# case=int(input())
# for i in range(case):
#     a,b=map(int, input().split())
#     print((a**b)%10)

case=int(input())
for i in range(case):
    a, b = map(int, input().split())
    a %=10
    if a==0:
        print(10)
    elif a==1 or a==5 or a==6:
        print(6)
    elif a==4 or a==9:
        b %=2
        if b==1:
            print(a)
        else:
            print((a*a)%10)
    else:
        b = b % 4
        if b == 0:
            print((a ** 4) % 10 % 10 % 10)
        else:
            print((a ** b) % 10 % 10 % 10)