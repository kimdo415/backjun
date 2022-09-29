# import itertools
# N,M=map(int, input().split())
# Nlist=[]
# for i in range(N):
#     Nlist.append(i+1)
# Nlist=list(itertools.permutations(Nlist,M))
# for i in Nlist:
#     print(' '.join(map(str,i)))
N,M=map(int, input().split())
vist=[False]*N
out=[]
def bact(depth, N , M):
    if depth==M:
        print(' '.join(map(str, out)))
        return
    for i in range(len(vist)):
        if not vist[i]:
            vist[i]=True
            out.append((i+1))
            bact(depth+1,N,M)
            vist[i]=False
            out.pop()
bact(0,N,M)