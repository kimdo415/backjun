case=int(input())

for i in range(case):
    list_s=list(map(str, input().split()))
    ans=0
    for i in range(len(list_s)):
        if i==0:
            ans += float(list_s[0])
        if list_s[i]=='@':
            ans *=3
        if list_s[i]=='#':
            ans -=7
        if list_s[i]=='%':
            ans +=5
    print("%0.2f" % ans)
