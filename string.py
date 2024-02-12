text = "Hello"
text1 = "THERE"

print(text)

# Accessing an element in a string
print(text[2])
print(text[4])

# Modifying a string
print(text.upper())
print(text1.lower())

# size/length of a string
print(len(text))

# String Concatination - combning strings (uses a plus symbol)
print(text + " " + text1)

# 1. Reassign a string

print(text)
text = "Hi there"
print(text)
# 2. Delete a string
del text
print(text)
