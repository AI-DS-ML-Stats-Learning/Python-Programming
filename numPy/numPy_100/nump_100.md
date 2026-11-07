np.where() -> to find the coordinates matching a condition in the array

np.where(condition, if_true, if_false)
This is very useful in general. It picks values element by element based on a condition:
arr = np.random.uniform(-10,10,10)
print(arr)
np.where(arr>0, np.ceil(arr), np.floor(arr))

np.copysign(np.ceil(abs(arr)), arr) -> copysign basically copies the origin sign (-ve/+ve) to the changed array

np.argwhere() -> same as above, but returns in pairs
np.argmax() -> coordinates/index of the max value in the array
np.argmin() -> coordinates/index of the min value in the array
np.unravel_index(nth_position, arr.shape) -> returns the coordinates/index of the nth position
np.ravel_multi_index(coordinates, arr.shape) -> returns the position of the index
np.matmul -> matrix multiplication

np.vstack -> stacks one array above another one of same size
np.hstack ->  stacks one array beside another one of same size
np.tile -> Thsi is also used for stacking or repeating an entire array. np.tile(arr,(4,4)) -> this basically repeats the entire array "arr" 4 times right and down.


For custom Data-Type Creation - 
Code	Meaning
np.int32 / "i4"	32-bit integer
np.float64 / "f8"	64-bit float
np.ubyte / "u1"	unsigned byte (0–255)
"U10"	text, up to 10 characters
np.bool_ / "?"	True/False

Floor division (//) - It divides and then rounds down to the nearest whole number.
7 / 2    # 3.5  → normal division
7 // 2   # 3    → floor division (3.5 rounded down)

Set Functions - 
Function	Returns	Result for a, b above
np.intersect1d(a, b)	values in both	[2 4 5] -> does not retains duplicates and neitehr the order
a[np.isin(a,b)] - returns matching values from a in the order (a set order) and also duplicates
np.union1d(a, b)	values in either	[1 2 3 4 5 7 9]
np.setdiff1d(a, b)	in a but not b	[1 3]
np.setxor1d(a, b)	in exactly one of them	[1 3 7 9]
np.unique(a)	unique values of a	[1 2 3 4 5]

np.emath.sqrt -> np.emath as a prefix means : emath (extended math) convert a number to complex when needed. Mostly used when a input is negative and it is bound to return nan on usual mathematical operations

a = a+2 -> 
    creates 2 memory blocks 
    1st memory will be for a+2
    2nd block will be for a
    this is how python works

a += 2 -> Python says to do the operation on the variable instead, so no new memory block is created

np.array_equal(a,b) -> compares two arrays and returns one True/False value

arr.flags.writeable = False -> this makes the array immutable (read-only), like a tuple, means values in this array can't be changed
print(arr.flags)
        C_CONTIGUOUS : True
        F_CONTIGUOUS : True
        OWNDATA : True
        WRITEABLE : False
        ALIGNED : True
        WRITEBACKIFCOPY : False

np.hypot(x, y) -> calculates hypotenuse: squareroot of x2 + y2
np.arctan2(y,x) -> calculates tan inverse of y/x

