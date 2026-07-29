words = ['apple', 'banana', 'cherry', 'date']


# Your Task: Write a single dictionary comprehension that maps each word to a list of its vowels (a, e, i, o, u).

{
    'apple': ['a', 'e'], 
    'banana': ['a', 'a', 'a'], 
    'cherry': ['e'], 
    'date': ['a', 'e']
}

var = {name:[j for j in name if j in ('a','e','i','o','u')] for name in words}

print(var)