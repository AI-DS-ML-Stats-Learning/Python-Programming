scores = {'Salil': 92, 'Amit': 45, 'Rahul': 78, 'Priya': 35}

# The student names remain the keys.
# The value is "Pass" if their score is 50 or above, and "Fail" if their score is below 50.

# new_dict = {i: 'Pass' if scores[i] >=50 else 'Fail' for i in scores}
new_dict = {name: 'Pass' if score >=50 else 'Fail' for name, score in scores.items()}

print(new_dict)