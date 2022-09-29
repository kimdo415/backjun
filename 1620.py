

# N,M=map(int, input().split())
# pm=list()
# for i in range(N):
#     pm.append(input())
# answ=[]
# for i in range(M):
#     ans=input()
#     if ans.isdigit():
#         answ.append(pm[int(ans)])
#     elif ans.isalpha():
#         answ.append(pm.index(ans))
# for i in answ:
#     print(i)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])