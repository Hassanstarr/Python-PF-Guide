# -------------------- DICTIONARY --------------------
print("\n--- Dictionary (key-value storage) ---")

student = {"name": "Hassan", "age": 20, "grade": "A"}
print("Original dictionary:", student)

# Update a value
print("\nUpdating age to 21...")
student["age"] = 21
print("After age update:", student)

# Add a new key-value pair
print("\nAdding city = Lahore...")
student["city"] = "Lahore"
print("After adding city:", student)

print()

# Loop through dictionary
print("\nDictionary items:")
for key, value in student.items():
    print(f"{key}: {value}")

print()

# -------------------- SET --------------------
print("\n--- Set (unique, unordered collection) ---")

numbers_set = {1, 2, 3, 3}  # duplicates removed automatically
print("Initial set:", numbers_set)

# Add a value
print("\nAdding 4...")
numbers_set.add(4)
print("After adding 4:", numbers_set)

# Remove a value
print("\nRemoving 1...")
numbers_set.remove(1)
print("After removing 1:", numbers_set)
print()

# Set operations
set_a = {1, 2}
set_b = {2, 3}

print("\nSet A:", set_a)
print("Set B:", set_b)

union_set = set_a | set_b
intersection_set = set_a & set_b

print("Union (A | B):", union_set)
print("Intersection (A & B):", intersection_set)
