"""

Assignment set on 28/05/2019

"""

instance = "Instance (noun): \n 1. a case or occurrence of something."

print(instance)

print(type(instance))

variable = 18

variable = 5*variable - 6

print(variable)

print(type(variable))

test1 = isinstance(instance, int)
test2 = isinstance(variable, int)

print("Is the definition of 'instance' an integer?")
print(test1)

print("Is my chosen variable an integer?")
print(test2)

"""

In python...

Variable: an name which can be associated with a particular piece of data. The data can be reassigned to the name without
requiring the name to be altered along with it.

Instance: refers to the current type or structure of data associated with a particular variable. The type() function can
return the type/class of the data. the isinstance() function will return T/F whether the given variable matches the given
data type.

String: a simple sequence of unicode characters. Functions can be used to return certain aspects of the string, be it the 
length or a specific character. Functions can also alter the text of a string - for instance, convert a text to upper case.

Integer: a numeric value with zero decimal places.

"""