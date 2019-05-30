# Lists in Python
# Keeps a list of objects ordered by index
# This might also be called an 'array' other programming languages

# To declare a list, use square brackets [.]
# Separate objects with commas

crazy_landlords = ['Jane', 'Mike', 'Cruella'] # Initial Declaration

print(crazy_landlords)
print(type(crazy_landlords))

# Accessing a list

# Call entries with the relevant index

print(crazy_landlords[1])
print(crazy_landlords[-1])

# Editing a list

# Assign a new value to a specific index

crazy_landlords[1] = 'Mike Tyson'
print(crazy_landlords)

# Adding more elements to a list
# Use .append()

crazy_landlords.append('Yuriy')
print(crazy_landlords)

# Removing elements of a list
# Use .pop()

crazy_landlords.pop(0)
print(crazy_landlords)




