import itertools

# counter = itertools.count(start=4, step=-5)

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# data = [100,200,300,400]

# daily_data = list(zip(itertools.count(), data))
# daily_data = list(zip(range(10), data))
# daily_data = list(itertools.zip_longest(range(10), data))

# print(daily_data)

# for i in daily_data:
#     print(i)
    # print(type(i))

# counter = itertools.cycle((1,2,3)) #can pass tuple, list

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# counter = itertools.repeat(4, times=3)

# squares = map(pow, range(10), itertools.repeat(3, times=5))
squares = itertools.starmap(pow, [(0,2),(1,2),(2,2),(3,2)])
squares = map(pow, range(10), [2]*10)

# print(list(squares))

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))