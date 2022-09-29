
N, M = map(int, input().split())
S = set()
for i in range(N):
    S.add(input())

S1 =set()
for i in range(M):
    S1.add(input())

ans=sorted(list(S&S1))
print(len(ans))
for i in ans:
    print(i)