# t=list(map(int, input().split()))
# t.sort()
# if (t[0]**2) + (t[1]**2)==(t[2]**2):
#     print('right')
# else:
#     print('wrong')
while True:
    t = list(map(int, input().split()))
    if max(t)==0:
        break
    t.sort()
    if (t[0]**2) + (t[1]**2)==(t[2]**2):
        print('right')
    else:
        print('wrong')
