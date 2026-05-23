# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

n = int(input())
n_list = list(input().split(" "))
k = int(input())

lst = []
for i in range(1,n+1):
    lst.append(i)

perm = itertools.combinations(lst, k)
ind = []
for c, i in enumerate(n_list, start=1):
    if i == 'a':
        ind.append(c)
        # print(c)

# print(ind)
count = 0
c = 0
for i in perm:
    c += 1
    for j in ind:
        if j in i:
            count += 1
            break

print(round(count/c,4))
