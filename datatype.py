# Data Types
number= 45 #int
bun =56.78 # float
greeting =("Hello there ") # str
isPythonInteresting = True # bool

# Variable storing multiple values
languages = ["Python", "php", "java"]
# LIST,
# uses special brackets,ordered,
# changable(can add or remove items in it after it has been created),
# allow duplicate items, items can be of any datatype
fruits = ("apple", "banana", "pineapple") # Tuple
countries = {"Kenya", "China", "USA"} # set
# Dictionary
details = {
    "firstname" : "Grace",
    "age" : 17,
    "course" : "MIT",
    "nationality" : "North America"

}
print(languages)
print(fruits)
print(details["course"])
print(number)
print(greeting)
print(isPythonInteresting)
print(details)

# Determining the data type
print(type(details))
print(type(countries))

# Type casting - Converting one datatype to another
print(float(number)) # Float is a decimal number
print(int(bun))