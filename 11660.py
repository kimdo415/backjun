import statistics

def m(al):
    l=len(al)%2
    if l==0:
        if al[len(al)//2]<al[len(al)//2-1]:
            return al[len(al)//2]
        elif al[len(al)//2]>al[len(al)//2-1]:
            return al[len(al)//2-1]
    elif l!=0:
        return statistics.median(al)

al=[]
n=int(input())
for i in range(n):
    b=int(input())

    print(al)
    print(m(al))