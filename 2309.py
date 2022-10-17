from itertools import combinations
small_dwerf=[int(input()) for _ in range(9)]
small_dwerf.sort()

for i in combinations(small_dwerf,7):
    if sum(i)==100:
        for j in i:
            print(j)
            break