temperature = 13
if temperature > 25:
    print("It is hot")
else:
    print("It is cold")

# A program that returns the largest number among three numbers
num1 = 45
num2 = 60
num3 = 20
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")

# A program that checks whether a number is even or odd
number = 0

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

    # A program that checks whether a number is prime or not
num = 30
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
# check for factors
    for i in range(2, num):
        if (num % i) == 0:
# if factor is found, set flag to True
            flag = True
            # break out of loop
            break
# check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

num8 = 893
if num8 == 1:
    print(num8, "is not a prime number")
elif num8 > 1:
    # check for factors
    for i in range(2, num8):
        if (num8 % i) == 0:
            print(num8, "is not a prime number")
            print(i, "times", num8 // i, "is", num8)
            break
    else:
        print(num8, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num8, "is not a prime number")

Num = 85
for i in range(2, Num):
    if (Num % i) == 0:
        print(Num, "is not a prime number")
        break
    else:
        print(Num, "is a prime number")