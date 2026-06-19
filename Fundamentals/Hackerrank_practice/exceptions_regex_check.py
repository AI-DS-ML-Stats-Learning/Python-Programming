# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

t = int(input())

for i in range(t):
    pattern = raw_input()
    try:
        re.compile(pattern)
        print("True")
    except re.error:
        print("False")
    
