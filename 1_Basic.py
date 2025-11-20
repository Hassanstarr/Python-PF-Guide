# A variable stores a value that you want to use later
# You simply write the name and give it a value

age = 18            # whole number
price = 99.99       # decimal number
name = "Hassan"     # text value
is_student = True   # true/false value

# Print the stored values
print(age, price, name, is_student)


# ==========================

# input() lets the user type something
# It always gives the result as text

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))  # changing text to number

# Showing the input back to the user
print("Hello", user_name)
print("You are", user_age, "year old")


# =========================

# Operators help us do calculations and comparisons

a = 15
b = 4

# Basic math operations
print(a + b)
print(a - b)
print(a * b)
print(a / b)       # division
print(a // b)      # division giving whole number
print(a % b)       # remainder
print(a ** b)      # a raised to the power b

# Checking conditions
print(a > b)
print(a == b)

# Logical operations
print(True and False)
print(True or False)
print(not True)
