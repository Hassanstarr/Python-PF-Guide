
# =======CONDITIONALS & LOOPS EXAMPLES=====

print("--- When to Use Conditionals ---")
print("if      : check a single condition")
print("if-else : choose between two outcomes")
print("if-elif-else : choose from multiple possibilities")
print("nested if : decision inside another decision")
print("match-case : cleaner alternative to many elif (Python 3.10+)\n")


# If / Elif / Else
marks = 85
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
else:
    grade = "Below A"

print(f"Marks: {marks} --> Grade using if-elif-else: {grade}")


# Nested If
if marks >= 50:
    if marks >= 90:
        nested_grade = "A+"
    else:
        nested_grade = "A"
else:
    nested_grade = "Fail"

print(f"Marks: {marks} --> Grade using nested if: {nested_grade}")


# For Loop
print("\nFor loop example (print numbers 0-4):")
for i in range(5):
    print(i, end=" ")
print()  # newline


# While Loop
print("\nWhile loop example (count down from 3):")
counter = 3
while counter > 0:
    print(counter, end=" ")
    counter -= 1
print()  # newline


# Do-While Equivalent
print("\nDo-while equivalent in Python (runs at least once):")
attempt = 1
while True:
    print(f"Attempt {attempt}: This runs at least once")
    condition_is_false = True  # simulate condition
    attempt += 1
    if condition_is_false:
        print("Condition failed, breaking loop")
        break
