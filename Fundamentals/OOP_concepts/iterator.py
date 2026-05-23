nums = [1,2,3]

# i_nums = nums.__iter__()
i_nums = iter(nums)

# print(i_nums)
# print(dir(i_nums))

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break