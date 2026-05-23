

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
n_eng = int(input())
n_roll = set(map(int, input().split(" ")))

b_french = int(input())
b_roll = set(map(int, input().split(" ")))

# for i in b_roll:
#     n_roll.add(i)


print(len(n_roll.symmetric_difference(b_roll)))
