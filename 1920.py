n=int(input())
nl=list(map(int, input().split()))
case=int(input())
anl=list(map(int, input().split()))
nl.sort()
for i in anl:
    if i in nl:
        print(1)
    else:
        print(0)