import itertools
import operator

letters = ['a', 'b', 'c', 'd']
numbers = [[1,2,3], [2,1,0]]
numbers1 = [[1,2,3], [2,1,0], [4,5,1], [3,7,1]]
names = ['Corey', 'Nicole']

# combined = itertools.starmap(sum, numbers) - takes only 2 arguments per list

# combined = itertools.zip_longest(numbers, numbers1)

# result = itertools.accumulate(numbers)
# result = itertools.accumulate(numbers, operator.mul)

# selectors = [True, True, False, True]

# result = itertools.compress(letters, selectors)

# for i in result:
#     print(i)

# result = itertools.permutations(letters, 2)
# result = itertools.permutations(numbers, 2)
# result1 = itertools.combinations(numbers, 2)
# result = itertools.product(numbers, numbers1, repeat=1)

# result = itertools.product(
#     [x for x in numbers[0][1:]],
#     [x for x in numbers[1][1:]], 
#     repeat=1)

sublist = [i[1:] for i in numbers1]
result = itertools.product(
   *sublist,
    repeat=1)

# result = itertools.combinations_with_replacement(numbers, 2)

# combined  = itertools.chain(letters, numbers, names)

# combined = itertools.islice(range(10), 5)

for item in result:
    print(item)

# print(combined)

