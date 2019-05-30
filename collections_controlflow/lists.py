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

# Lists can contain any objects
# e.g. string, int, float, bool, lists, dictionaries ect.

combined_list = [1, '10', 'ten', True, crazy_landlords]
print(combined_list)

# List slicing
# Allows you to manage a list

print(combined_list[0::2])

# ^ Double colon :: goes from the number before while taking every nth entry where n is the number after ::

print(combined_list[3:])

# ^ Empty space after colon prints from the first index to the end of the list

print(combined_list[1:3])

# ^ Specifying indices before and after gives the range between the two indices, not inclusive of the last index


