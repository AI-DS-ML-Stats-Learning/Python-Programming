Data Types

String - 
1. str.strip() - only removes trailing spaces
2. str.capitalize() - only capiatlizes the 1st letter of the sentence
3. str.title() - capitalizes the 1st letters of all the words in the input
4. str.split() - splits the sentence into words based on the delimiter (default = " ")

strings are immutable

Int

Float

functions -> main(), UDF()

variables

scope -> global, local

condtional operators
if else
if elif else
match [switch case]
continue
break

end keyword in print statement decides what should be appended to the end of a string

for
while

list [] -> slice
    list[start:end:step] -> where end index is exclusive + 'step' is the count of characters that will be skipped
    list[strt:end] -> where end index is exclusive
    list[-i:] -> where -1 is the last element of the list and moving on left the negative reduces to -2,-3, etc
    list[::-1] -> reverses the list. "::" means we are not defining start or end of list, hence whole list is considered. Now, -1 commands to go from the very end of the list and so it keeps moving to left as the iteration continues, hence the list reverses
    del list[1:4] -> deletes a subset of the list

dict {a:b, c:d}
    dict.items() -> unpacks and returns (key, value) pair
    dict.keys() -> returns all the keys
    dict.values() -> returns all the values
    dict.fromkeys() -> firstly it should be interpreted as dict.fromkeys(key,0) where we are creating a (key,value) pair with set of keys already there and pairing with a default "value = 0"
    dict.get() -> returns the value against the "key" mentioned
    dict.update() -> merges another dictionary/(key,value) pair to an existing one
    dict.pop() -> returns the last inserted value for a key and removed the key from the dict

exceptions - syntax error, error handling [ValueError, NameError, AssertionError]
    try
    except
    else
    pass
    raise

library
modules
packages -> PyPi
pip -> package manager to install packages
api - application programming interface
requests -> a python library that allows the users to do internet requests, means enables web requests

sys module -> argv, exit

assert -> keywprd to assert that something is true [throws error if false]
pytest -> does the tests for you, it is a 3rd party library

__init__.py -> this helps python to identify a folder to treat as a module/package in which this file exists

File I/O -> r,w,a

lambda -> lambda arguments: expression

csv -> .reader, .DictReader, .writer

regex -> re library for checking regular expressions or patterns
. -> represent any character except a newline
* -> 0 or more reps
+ -> 1 or more reps
? -> 0 or 1 reps
{m} -> m reps
{m,n} -> between m and n reps
^ -> start of the string
$ -> end of the string
[] -> set of characters
[^] -> complementing the set
\w -> any word character as well as an underscore and a number
\W -> not a word character
\d -> decimal digit
\D -> not a decimal digit
\s -> whitespace characters
\S -> not a whitespace character
A|B -> either A or B
(...) -> a group
(?:..) -> non-capturing version [basically ignore a parenthetical element as a part of group when extracted via matches.group() where matches stores the re.search() results]
re.IGNORECASE
re.MULTILINE
re.DOTALL
:= [The Walrus Operator] -> this assigns from right to left and also does a boolean check (for true or false)

tuple -> () [immutable [cannot change the values] ]

sets -> set()
    a.add(b)
    a.update(b)
    a.discard(b)
    a.remove(b)
    a.union(b)
    a.intersection(b)
    a.difference(b)
    a.symmetric_difference(b) -> exclusive to both the sets


constants

mypy -> function in python that catches exceptions
black -> format the .py file

typehints -> mention what value type does a function return (like int, str, None) + used to increase the readability of the code

docstrings -> """This is a docstring comment"""

argparse -> argument parser

unpacking -> *args [posittional arguments], **kwargs [keyword-arguments]
    *variable unpacks the elements of a list
    **variable unpacks the elements of a dictionary

map -> map(function, variable)

list comprehension
dictionary comprehension

filter -> filter(boolean function , variable) [the first argument will be msotly a fucniton that returns boolean value True
         and False to filter the variable]

enumerate -> fethces the value and the index of the elemeents in a variable

generators -> used using the keyword "yield"

iterators -> 
    object with a state that knows where it is during the iteration (__iter__) : iter(variable) 
    Iterators also know how to get the next value using (__next__) : next(variable)

zip -> 
    it basically pairs 2 or more variables together in the form of a tuple
    zip(x,y) -> this can be converted to list to be used as one 

IMP - 
itertools -> It is a collection of tools that allows us to work with iterators in a fast and memory-efficient way
    itertools.count(start, step) -> gives count
    .zip_longest(range(), var) -> continues to zip until the last value of the range/last index [pairs corresponding index]
    .cycle -> next cycles back to 1st value once the range/list input has come to an end
        map(pow, bases, exponents) -> here exponents cam be replaced with itertools.cycle(2) where 2 will indicate the power to the function
    .repeat ->  basically it tells how many repititions should be done of the input values
        map(pow, bases, exponents) -> here exponents cam be replaced with itertools.repeat(2) where 2 will indicate the power to the function
    .starmap -> it takes tuples as inputs that are already paired
        itertools.starmap(pow, [(0,2),(1,2),(2,2),(3,2)])
    .combinations -> generates all possible unique pairs (where (1,0) and (0,1) are considered same) and also excludes self pair like (0,0), (1,1)
        itertools.combinations([0,1,2], 2) -> (0,1), (0,2), (1,2)
    .permutations -> generates all possible pairs except pairing with self like (0,0), (1,1)
        itertools.permutations([0,1,2], 2) -> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)
    .product -> generates cartesian products, basically all possible pairs where self pairs also includes
        itertools.product(numbers, repeat=4) -> group in the size of 4 elements and then generate the combinations
        itertools.product([0,1,2], repeat=2) -> (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)
        ## THIS CAN CREATE COMBINATIONS WITH MULTIPLE LISTS
    .combinations_with_replacement -> generates all possible unique pairs (where (1,0) and (0,1) are considered same) but here it includes self pair like (0,0), (1,1)
        itertools.product(numbers, repeat=4) -> group in the size of 4 elements and then generate the combinations
        itertools.product([0,1,2], repeat=2) -> (0,0), (0,1), (0,2), (1,1), (1,2), (2,2)
    .chain -> combines values of different variables into one. Variables can be combined simpy by using '+' sign but in case of large data it won't be efficient, hence .chain is used there
    .islice -> slice itertools items. list slicing can also be used here but again for a variable/data size with high number, list slicing will be an expensive and slow process, hence itertools can be used here.
        itertools.islice(range(10),1,5, 2) -> 1 is the start, 5 is the end and 2 is the step
    .compress -> It takes two iterables:
        data: the sequence of values you want to filter.
        selectors: a sequence of truthy/falsey values (like 1/0 or True/False).
        It yields elements from data only where the corresponding selector is true.
        itertools.compress(letters, selectors) -> selectors = [True, True, False, True] and letters = ['a', 'b', 'c', 'd']. This only filters for letterrs which have corresponding True values.
        THIS IS SIMILAR FUNCTION TO FILTER
    .filterfalse -> works like filter/compress but returns all the values where the boolean is false
    .dropwhile -> this also works like filter but it breaks the function once the 1st value is found that satisifies False boolean condition. Post that all the values are included.
        refer 'filter.py' file in OOP_concepts
    .takewhile -> works like filter/compress but returns all the values that are marked as True but breaks out of the function as soon as the 1st False is encountered
        refer 'filter.py' file in OOP_concepts
    .accumulate -> returns cumulative sum at each row until last element is reached. The same function can be changed to give cumulative product or any other math operation using 'operator'
        itertools.accumulate(numbers) -> numbers = [0,1,2,3] it returns 0, 1, 3, 6
        itertools.accumulate(numbers, operator.mul) -> numbers = [1,2,3, 4] it returns 1, 2, 3, 6, 24
    .groupby -> groups consecutive elements of an iterable based on a key function, returning (key, group) pairs where each group is itself an iterator. The critical detail is that grouping only happens for adjacent items — so if your data isn’t sorted by the key, you won’t get the grouping you expect.
        refer to itertools_groupby.py in OOP_concepts
    .tee -> creates copies of a iterator which can be later used. Once a copy is created, the original iterator should nto be used, else the data will be used and once used, the copy iterators reference point will also be empty

collections

functools -> modules in python that enables functional programming in python easier to implement - "higher-order functions—functions that act on, modify, or return other functions."
    reduce(func, iterable, initializer = None) - is used to apply a function (func) of two arguments cumulatively to the items of an iterable (like a list) from left to right, reducing the sequence to a single value.

pathlib

