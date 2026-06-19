# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for i in range(n):
    string = input()
    pattern = re.findall(r'(\<\/?[a-zA-Z0-9\=\-\' ]+\/?\>)', string)
    j = []
    if pattern:
        for p in pattern:
            if new:=re.findall(r'\<([a-zA-Z0-9\=\-\' ]+)\>', p):
                # print(f"Start : {new}") 
                for i in new:
                    if " " in i:
                        # for el in i:
                        #     j.append(el)
                        i = i.split(" ")
                        for index, k in enumerate(i, start = 1):
                            if index ==1:
                                print(f"Start : {k}")
                            else:
                                if "=" not in k:
                                    print(f"-> {k} > None")
                                else: 
                                    final = k.split("=")
                                    print(f"-> {final[0]} > {final[1].strip(" '")}")
                    else:
                        print(f"Start : {i}") 
            elif re.findall(r'^\<\/', p):
                print(f"End   : {p.strip("</>")}")
            elif re.findall(r' \/\>$', p):
                print(f"Empty : {p.strip("</>")}")
