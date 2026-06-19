# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 

t = int(input())

for i in range(t):
    pattern = input()
    if re.search(r'^[+|-]?[0-9]*\.[0-9]+$', pattern):
        print("True")
    else:
        print("False")
