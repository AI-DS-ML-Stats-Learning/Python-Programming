# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

k,m = list(map(int, input().split(" ")))
j = []
for i in range(k):
    j.append(list(map(int, input().split(" "))))


square_of_list = []
for i in j:
    square_of_list.append(list(map(pow, i[1:], [2]*10)))
    
sublist = [i for i in square_of_list]

product = itertools.product(*sublist, repeat = 1)
k = []
for i in product:
    k.append(tuple(i))
# print(k)    
    
# sum_of_products = itertools.starmap(sum, k) - starmap will throw an error as by def a sum  = a+b which means only values for sum function even within a list, the number of elements should be 2 in each sublist/list
sum_of_products = list(map(sum, k))

# print(sum_of_products)

# find the largest
a = sum_of_products[0]%m
for i in sum_of_products[1:]:
    if i%m>a:
        a = i

print(j)
print(square_of_list)
print(sum_of_products[0])
print(m)
print(a)