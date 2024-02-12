# Inbuilt functions
number = max(89, 70, 49, 123)
print(number)

x = min(89, 78, 45, 23, 1)
print(x)

z = pow(2, 3)
print(z)


# User-defined functions
def name():
    print("Holliness")


name()  # Calling a function


def student():
    name = "Vincent"
    age = 18
    course = "MIT"
    print(name, age, course)


student()


# Parameters/ variables and arguments/values
def students(name, age, course):
    print(name, age, course)


students("Vincent", 18, "MIT")
students("Grace", 17, "Cybersecurity")
students("Grace", 17, "Cybersecurity")
students("Grace", 17, "Cybersecurity")
students("Grace", 17, "Cybersecurity")
students("Grace", 17, "Cybersecurity")
students("Grace", 17, "Cybersecurity")
students("Vincent", 18, "MIT")
students("Vincent", 18, "MIT")
students("Vincent", 18, "MIT")


# Create a user-defined function
# called employees. It should display
# details of five employees. Parameters are:
# fullname, age, gender, position, salary


def employees(fullname, age, gender, position, salary):
    print(fullname, age, gender, position, salary)


employees("Mark Sloan", "35", "male", "Managing director", "250,000")
employees("Jane Doe", "22", "female", "Secretary", "200,000")
employees("Luke Montgomery", "25", "male", "Accountant", "150,000")
employees("Issa Nisha", "30", "female", "sales representative", "100,000")
employees("Keller Brownstone", "27", "male", "Customer Service", "50,000")
