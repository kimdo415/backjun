a=[5,7,5]
b=[5,5,7]

for i in range(3):
    if a.count(a[i])==1:
        k=a[i]
    if b.count(b[i])==1:
        t=b[i]
print(k,t)


    # if b.count(b[i])==1:
    #     print(b[i])

# for i in range(3):
#     x,y=map(int, input().split())
#     a.append(x)
#     b.append(y)
# print(a,b)
