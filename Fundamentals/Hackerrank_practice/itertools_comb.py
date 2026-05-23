# Enter your code here. Read input from STDIN. Print output to 
import itertools

s = input()
a, k = s.split(" ")
a = sorted(list(a.upper()))
k = int(k)
# print(list(a))

for i in range(1, k+1):
    comb = itertools.combinations(a, i)
    # lst = []
    for j in [list(x) for x in comb ]:
        # print(split_and_join(j))
        print(''.join(j))
