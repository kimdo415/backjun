cham=int(input())
w=[]
h=[]
move=6
for i in range(move):
    v,cm=map(int, input().split())
    if v==1 or v==2:
        w.append(cm)
    if v==3 or v==4:
        h.append(cm)
print((max(w)*max(h)-min(w)*min(h))*cham)
