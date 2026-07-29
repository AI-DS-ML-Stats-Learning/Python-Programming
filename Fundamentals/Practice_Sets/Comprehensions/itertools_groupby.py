transactions = [
    {'type': 'buy', 'amount': 100},
    {'type': 'sell', 'amount': 150},
    {'type': 'buy', 'amount': 50},
    {'type': 'buy', 'amount': 200},
    {'type': 'sell', 'amount': 300}
]

# What is the strict rule we must follow on the transactions list before passing it to itertools.groupby()? - we need to order by based on the key which we want to groupby
# Write the code to group the transactions by 'type' and print them.

sorted_dict = sorted(transactions, key = lambda s:s['type'])

import itertools

grouped = itertools.groupby(sorted_dict, key  = lambda s : s['type'])

for key, group in grouped:
    print(key, list(group))