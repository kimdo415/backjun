a=int(input())

for i in range(a):
    r,e,c=map(int, input().split())
    if r<e-c:
        print('advertise')
    if r==e-c:
        print('does not matter')
    if r>e-c:
        print('do not advertise')