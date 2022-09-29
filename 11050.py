def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
N,K=map(int, input().split())
print(int(fact(N)/(fact(K)*fact(N-K))))