case=int(input())
vote=list(str(input()))

if vote.count('A')>vote.count('B'):
    print('A')
if vote.count('A')<vote.count('B'):
    print('B')
if vote.count('A')==vote.count('B'):
    print('TIE')

