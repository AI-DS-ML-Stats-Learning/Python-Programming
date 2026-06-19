# Enter your code here. Read input from STDIN. Print output to STDOUT
import re 

n = int(input())

s = []
if 0<n<50:
    for i in range(n):
        s.append(input().strip())
scalp = "\n".join(s)

pattern = re.findall(r'\{([^{}]+)\}', scalp)

for i in pattern:
    check = re.findall(r'(\#[0-9a-fA-F]{6}|\#[0-9a-fA-F]{3})', i)
    for i in check:
        print(i)

