n = int(input())
s = set(map(int, input().split()))

n_ = int(input())

actions = []
for i in range(n_):
    actions.append(input())
    
# for i in actions:
#     print(len(i.split(" ")), i)
    
for i in actions:
    if len(i.split(" ")) == 1:
        a=i
    else:
        a,b = i.strip().split(sep=" ", maxsplit=1)
    
    if a == "pop":
        if not s:
            raise KeyError("pop from an empty set")
        else:
            s.pop()
    elif a=="remove":
        if int(b) not in s:
            raise KeyError(int(b))
        else:
            s.remove(int(b))
    else:
        s.discard(int(b))

a = 0
for i in s:
    a = a+i

print(a)

