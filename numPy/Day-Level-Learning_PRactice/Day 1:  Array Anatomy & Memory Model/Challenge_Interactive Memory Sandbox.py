import sys
import numpy as np

'''Python approach'''
my_list = []

for i in range(1,11):
    my_list.append(i)
    print(sys.getsizeof(my_list))

'''numPy approach'''
my_arr = np.array([], dtype = np.int32)

for i in range(1,11):
    my_arr = np.append(my_arr, i)
    print(my_arr.nbytes)

print(my_arr)