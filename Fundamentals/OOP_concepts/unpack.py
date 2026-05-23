"""unpacking using *args"""
def total(galleons=20, sickles=20, knuts=20):
    return (galleons*17 + sickles) * 29 + knuts

coins = [100,50,25]

# print(total(coins[0], coins[1], coins[2]), "knuts") 

print(total(*coins), "knuts") ##*coins unpacks the elements of the list


"""unpacking using **kwargs"""
def total1(galleons=20, sickles=20, knuts=20):
    return (galleons*17 + sickles) * 29 + knuts

coins= {"galleons":100, "sickles":50, "knuts":25}

print(total1(**coins), "knuts") ##**coins unpacks the elements of a dictionary


"""using *args and **kwargs in fucntions"""

def f(*args, **kwargs):
    # print("Keyword Arguments:", args)
    print("Keyword Arguments:", kwargs)


# f(100,25,50, 5)
f(galleons=20, sickles=20, knuts=20)
