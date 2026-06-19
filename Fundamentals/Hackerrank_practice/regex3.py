# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()

if len(s)>0 and len(s)<100:
    m = re.findall(r'([a-zA-Z0-9])\1+',s)
# print(m)
if not m: #checking list is empty or not
    print(-1)
else:
    print(m[0])