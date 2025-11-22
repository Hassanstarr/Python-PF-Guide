# Basic Function
def greet():
    print("Hello!")

# Function with parameters
def add(a, b):
    return a + b

# Default Arguments
def welcome(person="User"):
    print("Welcome,", person)


greet()

sum = add(5, 7)
print(f'The sum is {sum}')

welcome()
welcome("Hassan")

print()

# Scope
# Shadowing: local variable with same name as global
x = "Global X"

def shadow_example():
    x = "Local X"  # This does NOT change the global x
    print("Inside shadow_example -> x:", x)

print("Before calling function -> x:", x)
shadow_example()
print("After calling function  -> x still global:", x)

# Modifying a global variable (use global keyword)
count = 0

def increment():
    global count
    count += 1

increment()
increment()
print("Global count after increment:", count)