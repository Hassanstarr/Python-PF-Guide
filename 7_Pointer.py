# -------------------- MUTABILITY & REFERENCES --------------------
print("\n--- Mutable vs Immutable Objects ---")

# Mutable Example (List)
print("\nMutable Example (List):")
a_list = [1, 2, 3]
b_list = a_list  # both refer to the SAME list in memory

print("Original a_list:", a_list)
print("Original b_list:", b_list)

print("\nAppending 4 to b_list...")
b_list.append(4)

print("After change -> a_list:", a_list)  # also changed
print("After change -> b_list:", b_list)


# Immutable Example (Integer)
print("\nImmutable Example (Integer):")
x = 10
y = x  # y gets a copy of the value (integers are immutable)

print("Original x:", x)
print("Original y:", y)

print("\nIncreasing y by 5...")
y += 5  # creates a *new* integer object for y

print("After change -> x (unchanged):", x)
print("After change -> y:", y)
