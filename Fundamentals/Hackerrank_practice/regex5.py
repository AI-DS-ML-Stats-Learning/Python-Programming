# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
# import itertools

s = input().strip()
k = input().strip()
# k1 = 'r'+ '\'('+ k +')\''
# print(k1)

if (0< len(s)<100) and (0 < len(k)<len(s)):
    pattern = list(re.finditer(r'(?=('+k+'))', s))

if not pattern:
    print((-1,-1))
else:
    for p in pattern:
        index = tuple([p.start(1), p.end(1)-1])
        print(index)