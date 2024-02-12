# While loop
# incrementing a number - you must have a condition
number = 5 # initialize first value
while number <= 10: # set condition
    print(number)
    number += 1 #

# Decrement
num = 105
while num >= 100:
    print(num)
    num -= 1

# Break Statement
x = 20
while x <= 25:
    print(x)
    if x ==24:
        break # the program stops at 24
    x += 1

# Continue Statement
y = 79
while y < 85:
    y += 1 # increase the number b4 printing as we started with 79
    if y == 83:
        continue # it basically means skip
    print(y)

# For loop-you don't have a condition
# print out a range of elements
languages = ["Python", "Java", "C++"]
for z in languages:
    print(z)

# Range
for mynumber in range(5):
    print(mynumber)

for mynum in range(2, 6):
    print(mynum)

for count in range(20, 30, 2):# the last number is 2 which means that the printed numbers will increase by two
    print(count)