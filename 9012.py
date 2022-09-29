case=int(input())
for i in range(case):
    s=[]
    st=input()
    for i in st:
        if i=="(":
            s.append(i)
        elif i==")":
            if len(s) ==0:
                s.append(')')
                break
            else:
                s.pop()
    if len(s)==0:
        print("YES")
    else:
        print("NO")
            
            