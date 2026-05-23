import itertools

def lt_2(n):
    if n < 2:
        return True
    else:
        return False

numbers = [0,1,2,3,2,1,0]

# result = filter(lt_2, numbers)
# result = itertools.filterfalse(lt_2, numbers)
# result = itertools.dropwhile(lt_2, numbers)
result = itertools.takewhile(lt_2, numbers)


for i in result:
    print(i)