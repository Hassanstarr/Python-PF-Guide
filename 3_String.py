text = "Python Basics"

# Indexing & Slicing
first_char = text[0]
print(first_char)

slice_part = text[0:6] # 'Python'
print(slice_part)

# String Methods
lowercase = text.lower()
print(lowercase)

uppercase = text.upper()
print(uppercase)

count_letter = text.count("a")
print(count_letter)

replaced_string = text.replace("Basics", "Guide")
print(replaced_string)


# Looping over string
for ch in text:
    print(ch, end="")
    pass