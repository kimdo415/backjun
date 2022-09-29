print('케이스 입력:')
case=int(input())
for i in range(case):
    print('학교 숫자 입력')
    sn = int(input())
    a = []
    b = []
    for j in range(sn):
        print('학교와 술소비량 입력')
        sch,sul=map(int, input().split())
        a.append(sch)
        b.append(sul)
    dic={name:value for name, value in zip(a,b)}
    max_key=max(dic, key=dic.get)
    print(dic)
    print(max_key)
