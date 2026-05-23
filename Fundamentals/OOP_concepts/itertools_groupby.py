import itertools

def get_state(person):
    return person['state']

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

people_sorted = sorted(people, key= lambda s: s["state"])
person_group = itertools.groupby(people_sorted, get_state)

for key, group in person_group:
    print(key, len(list(group)))
    # for person in group:
    #     print(person)
    # print()

num_group = itertools.groupby(sorted(list([3,1,2,4,1,5,2,6,6,4,3,3,4])))

# for key, group in num_group:
#     print(key, list(group))
    # print(group)

copy1, copy2 = itertools.tee(num_group)
print()
# for key, group in num_group:
#     print(key, list(group))
#     print("num_group")
    
for key, group in copy1:
    x = list(group)
    print(key, len(x))
    print("copy1")

for key, group in copy2:
    print(key, len(list(group)))
    print("copy2")