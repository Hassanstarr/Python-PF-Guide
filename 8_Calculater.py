# -------------------- Calculator --------------------
print("\n--- Simple Calculator ---")

def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Invalid operator"

# Demo

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"\nInputs: a = {a}, b = {b}")

print("a + b =", calculator(a, b, "+"))
print("a - b =", calculator(a, b, "-"))
print("a * b =", calculator(a, b, "*"))
print("a / b =", calculator(a, b, "/"))
print("Invalid operator test:", calculator(a, b, "%"))