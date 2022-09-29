def solution(num):
    k=[1]
    for i in range(2,num):
        if num%i==0:
            k.append(i)
    if sum(k)==num:
        print(num, " = ", " + ".join(str(i) for i in k), sep="")
    else:
        print(num, "is NOT perfect.")

while True:
    num=int(input())
    if num==-1:
        break
    else:
        solution(num)



