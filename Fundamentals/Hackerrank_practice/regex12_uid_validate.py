# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    t = set(input())
    value = "".join(t)
    # print(value)
    if re.fullmatch(r'[a-zA-Z0-9]{10}', value):
        if re.findall(r'[A-Z].*[A-Z]', value):
            if re.findall(r'[0-9].*[0-9].*[0-9]',value):
                print("Valid")
            else:
                print('Invalid')
        else:
            print('Invalid')           
    else:
        print('Invalid')