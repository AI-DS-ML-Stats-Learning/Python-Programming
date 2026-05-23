import re

def minion_game(string):
    # your code goes here
    k = 1
    chunk = []
    while k<=len(string):
        for i in range(0,len(string)):
            if len(string[i:i+k]) == k:
                chunk.append(string[i:i+k])
        # print(chunk)
        k += 1
    # print(chunk)
    
    chunk = map(str.upper, chunk)
    
    Kevin = 0
    Stuart = 0
    for i in chunk:
        if re.search(r"^(A|E|I|O|U)", i[0]):
            Kevin += 1
        else:
            Stuart += 1
    if Kevin > Stuart:
        print(f"Kevin {Kevin}")
    elif Kevin < Stuart:
        print(f"Stuart {Stuart}")
    else:
        print("Draw")
        

if __name__ == '__main__':
    s = input()
    minion_game(s)


# ------OPTIMIZED VERSION

def minion_game(string):
    vowels = "AEIOU"
    Kevin = 0
    Stuart = 0
    
    for i in range(len(string)):
        if string[i] in vowels:
            Kevin += len(string) - i
        else:
            Stuart += len(string) - i
    
    if Kevin > Stuart:
        print(f"Kevin {Kevin}")
    elif Stuart > Kevin:
        print(f"Stuart {Stuart}")
    else:
        print("Draw")
        

if __name__ == '__main__':
    s = input()
    minion_game(s)