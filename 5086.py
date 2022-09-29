
# while True:
#     x,y=map(int, input().split())
#     if x == 0 and y == 0:
#         break
#     else:
#         print(x//y)
#         print(x%y)

while True:
    x,y=map(int, input().split())
    if x == 0 and y == 0:
        break
    if x>y:
        if x%y==0 and x//y !=0:
            print('multiple')
        else:
            print('neither')
    if x<y:
        if y%x==0 and y//x !=0:
            print('factor')
        else:
            print('neither')