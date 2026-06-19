# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
ab = []
for _ in range(t):
    # ab.append(list(map(int, input().split())))
    ab.append(input())

# print(ab)

for i in ab:
    a,b = i.split(" ")
    
    try:
        a = int(a)
        b = int(b)
        if b ==0:
            raise ZeroDivisionError("integer division or modulo by zero")
        print(int(a/b))
    except ValueError as e:
        # print("Error Code: invalid literal for int() with base 10:", b)
        print("Error Code:", e)
    except ZeroDivisionError as e:
        print("Error Code:",e)



"""if i have to show the error type as well in the user console"""
# except ZeroDivisionError as e:
#     print(type(e).__name__, "-", e)
