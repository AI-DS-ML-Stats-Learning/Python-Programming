if __name__ == '__main__':
    list1 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        list1.append([name,score])
    
    scores = [s[1] for s in list1]
    
    scores = sorted(set(scores))[1]
    
    final =[s[0] for s in list1 if s[1] == scores]
    
    for i in sorted(final):
        print(i)


