# multipliers = [lambda x: x * i for i in range(3)]
# print([m(10) for m in multipliers])

multipliers = [lambda x, i=i: x * i for i in range(3)]
print([m(10) for m in multipliers])

