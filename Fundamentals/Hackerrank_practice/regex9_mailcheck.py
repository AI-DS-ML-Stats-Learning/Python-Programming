# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

if 0<n<100:
    for i in range(n):
        s = input()
        name, mail = s.split('<')
        mail = mail.strip('>')
        p = re.fullmatch(r'[a-zA-Z](\w|\.|-)+@[a-zA-Z]+\.[a-zA-Z]{1,3}',mail)
        if p:
            print(s)
        # print(mail)
        # print(p)