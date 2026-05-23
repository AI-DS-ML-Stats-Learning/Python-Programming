# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
b = set(map(int, input().split(" ")))

n = int(input())

for i in range(n):
    x = list(input().split(" "))
    y = set(map(int, input().split(" ")))
    if x[0] == "intersection_update":
        b.intersection_update(y)
    elif x[0] == "update":
        b.update(y)
    elif x[0] == "symmetric_difference_update":
        b.symmetric_difference_update(y)
    elif x[0] == "difference_update":
        b.difference_update(y)
# print(x[0])
z = 0
for i in b:
    z += i

print(z)