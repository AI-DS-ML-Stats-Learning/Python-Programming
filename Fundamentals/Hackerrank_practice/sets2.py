# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

stamps = []
for i in range(n):
    stamps.append(input())
    
print(len(set(stamps)))