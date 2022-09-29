b=int(input())
a=list(map(int, str(b)))

while True:
    flag=True
    for i in str(b):
        if i !='4' and i !='7':
            flag=False
            b -=1
    if flag:
            break
print(b)

