# Enter your code here. Read input from STDIN. Print output to STDOUT
set_a = set(map(int, input().split(" ")))

n = int(input())

true_c = 0
false_c = 0
for i in range(n):
    set_x = set(map(int, input().split(" ")))
    
    if len(set_x) >= len(set_a):
        false_c = 1
    else:
        a = 0
        for x in set_x:
            if x in set_a:
                a += 1
            else:
                break
        if a == len(set_x):
            true_c +=1
        else:
            false_c +=1

if true_c == n:
    print("True")
else:
    print("False")
                