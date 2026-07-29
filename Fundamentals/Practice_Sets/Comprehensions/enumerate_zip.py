subjects = ["Math", "Physics", "Chemistry"]
scores = [90, 85, 95]

# Your Task: Write a single comprehension that outputs a list of formatted strings:
#        ['1. Math: 90', '2. Physics: 85', '3. Chemistry: 95']

# Hint: Think about how you can wrap zip() inside enumerate(),
#  and how you would unpack them in the for clause of your comprehension! Give it a try!

# var = [f"{i[0]}. {i[1]}: {k}" for i, k in list(zip(enumerate(subjects, start=1), scores))]

# var = [f"{id}. {sub}: {k}" for (id, sub), k in list(zip(enumerate(subjects, start=1), scores))]

var = [f"{id}. {sub}: {k}" for (id, sub), k in zip(enumerate(subjects, start=1), scores)]



# j = list(zip([i for i in enumerate(subjects, start=1)],scores))

print(var)