N,M=map(int,input().split())
S=set()
S1=set()
for i in range(N):
    S.append(input())

for i in range(M):
    S1.append(input())
c=0
for i in range(len(S1)):
    for j in range(len(S)):
        if S[j]==S1[i]:
            c+=1
print(c)