n,m=list(map(int, input().split()))
v=[]
def dfs(start):
    if len(v)==m:
        print(' '.join(map(str, v)))
        return
    for i in range(start, n+1):
        if i not in v:
            v.append(i)
            dfs(i+1)
            v.pop()
dfs(1)