# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()

if len(s)>0 and len(s)<100:
    pattern  = re.findall(r'(?=[^aeiouAEIOU]([aeiouAEIOU]{2,})[^aeiouAEIOU])',s)

if not pattern:
    print(-1)
else:
    for i in pattern:
        print(i)