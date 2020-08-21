# Python Booleans
# You can evaluate any expression in Python, and get one of two values
# -- True -- False

# Evaluate Values and Variables
# bool() -- allows you to evaluate any value
# Most Values are True
# False Values:
# -- empty strings
# -- 0
# -- None
# -- empty: - list - tuple - set - dictionary
# An object that is made from a class with a __len__ function
# -- Returns 0 or False

class my_class():
    def __len__(self):
        return 0

my_obj = my_class()
print(bool(my_obj))

# isinstance(): used to determine if an object is of a certain data type
x = 200
print(isinstance(x, int))
