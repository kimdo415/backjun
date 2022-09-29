# import math
#
# N,K=map(int, input().split())
# al=list(str(int(math.factorial(N)/(math.factorial(K)*math.factorial(N-K)))))
# al.reverse()
# c=0
# for i in range(len(al)):
#     if al[i]=='0':
#         c +=1
#     if al[i]!='0':
#         break
# print(c)

N,M=map(int, input().split())
def solution(n,k):
    c=0
    while n:
        n//=k
        c+=n
    return c
fc=solution(N,5)-solution(M,5)-solution(N-M,5)
tc=solution(N,2)-solution(M,2)-solution(N-M,2)
print(min(fc,tc))