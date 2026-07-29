users = [
    {'id': 1, 'name': 'Salil'},
    {'id': 2, 'name': 'Amit'},
    {'id': 3, 'name': 'Rahul'}
]

statuses = {
    1: 'active', 
    2: 'inactive', 
    3: 'active'
}

# Your Task: Write a single list comprehension that:

# Filters the users to find only those whose status is 'active' in the statuses dictionary.
# Returns a list of their names.
# Example Output: ['Salil', 'Rahul']

# Give it a try! Think about how you will look up the status using the user's 'id' in the dictionary.
# id_a = []
# for i in statuses:
    # print(i['active'])
#     print(statuses[i])
    # if j == 'active':
    #     id_a.append(i)

# lst_n = []
# for i in users:
#     if i['id'] in id_a:
#         lst_n.append(i['name'])

'''time complexity = O(m*n)'''
# var = [i['name'] for i in users for j, k in statuses.items() if k =='active' if i['id'] == j]

'''time complexity = O(n)'''
var = [i['name'] for i in users if statuses.get(i['id']) =='active']

# print(id_a)
print(var)