# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())

if 1<=n<=10:
    for i in range(n):
        s = input()
        if 1<=len(s)<=15:
            if re.fullmatch(r'(7|8|9){1}[0-9]{9}',s):
                print('YES')
            else:
                print('NO')