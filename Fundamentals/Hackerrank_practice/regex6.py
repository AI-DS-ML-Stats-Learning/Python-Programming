# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

def change(value):
    if value.group(0) == '&&':
        return 'and'
    else:
        return 'or'

if 0<n<100:
    for i in range(n):
        string = input()
        # print(re.sub(r'(( && )|( \|\| ))',change, string))
        print(re.sub(r'(?<= )(&&|\|\|)(?= )',change, string))
