# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
x = input().split(" ")
n2 = int(input())
y = input().split(" ")

i = list(map(int, x))
j = list(map(int, y))

i = set(i)
j = set(j)

i_diff_j = i.difference(j)
j_diff_i = j.difference(i)

for _ in j_diff_i:
    i_diff_j.add(_)

for a in sorted(i_diff_j):
    print(a)
# final1 = sorted(set(i))

# for _ in final1:
#     print(_)