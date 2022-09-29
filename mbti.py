survey=["AN", "CF", "MJ", "RT", "NA"]
choice=[5,3,2,7,5]
answer = ''
dic_mb= {'A' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'N' : 0, 'R' : 0, 'T' : 0}

for i in range(len(survey)):
    if choice[i]-4<0:
        dic_mb[survey[i][0]] += 4-choice[i]
    elif choice[i]-4>0:
        dic_mb[survey[i][1]] += choice[i]-4

answer += 'R' if dic_mb['R'] >= dic_mb['T'] else 'T'
answer += 'C' if dic_mb['C'] >= dic_mb['F'] else 'F'
answer += 'J' if dic_mb['J'] >= dic_mb['M'] else 'M'
answer += 'A' if dic_mb['A'] >= dic_mb['N'] else 'N'
print(answer)