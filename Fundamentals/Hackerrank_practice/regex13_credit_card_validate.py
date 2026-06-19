# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    card = input()
    if re.fullmatch(r'[0-9]{4}\-?[0-9]{4}\-?[0-9]{4}\-?[0-9]{4}', card):
        if re.findall(r'^(4|5|6){1}.*', card):
            card = "".join(card.split("-"))
            # card = card.replace("-","")
            if not re.findall(r'([0-9])\1{3,}', card):
                print("Valid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")