# Scenario: You want to create a lightweight data structure to store employee records. 
# You want the records to be immutable (so they cannot be modified after creation to prevent bugs) and highly memory-efficient.

# Your Task:

# Import namedtuple from collections.
# Define a namedtuple subclass named Employee with fields: name, age, department, salary.
# Instantiate it for an employee: "Salil", 28, "Engineering", 100000 and save it to the variable emp.
# Print the employee's name and salary using attribute dot access (like emp.name, not indexing like emp[0]).
# Conceptual Question: What happens if you try to update the salary using emp.salary = 120000? Why?
# Give it a shot! Think about how you define the namedtuple template first.

from collections import namedtuple

Employee = namedtuple("Employee", ("name", "age", "departmwent", "salary"))

emp = Employee("Salil", 28, "Engineering", 100000)

print(f"Employee's name: {emp.name}")
print(f"Employee's Salary: {emp.salary}")

# emp.salary = 1200000 #THis will not update the values since tupples are immutable

# Create a NEW employee object with the updated salary
updated_emp = emp._replace(salary=120000)

print(emp.salary)          # Output: 100000 (original is unchanged!)
print(updated_emp.salary)  # Output: 120000 (new object has the updated value)