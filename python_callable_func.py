print("---= Callables Operators =---")

print("-- *(tuple packing) --")
# Description: Packs the consecutive function positional arguments into a tuple.
# Syntax: def function(*tuple):
# -- tuple: A tuple object used for storing the passed in arguments.
# All the arguments can be accessed within the function body the same way as with any other tuple.
# Remarks: The tuple name *args is used by convention.

# Example:
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

x = add(1, 2, 3)
print(x)

print("*************************")

print("-- **(dictionary packing) --")
# Definition: Packs the consecutive function keyword arguments into a dictionary.
# Syntax: def function(**dict):
# -- dict: A dictionary object used for storing the passed in arguments.
# All the arguments can be accessed within the function body with the same way as with any other dictionary.
# Remarks: The dict name **kwargs is used by convention.

# Example:
def example(**kwargs):
    return kwargs.keys()

d = example(a = 1, b = 20, c = [10, 20, 30])
print(d)

print("*************************")

print("-- *(tuple unpacking) --")
# Definition: Unpacks the contents of a tuple into the function call
# Syntax: function(*iterable)
# Remarks:

# Example:
def add(a, b):
    return a + b

t = (2 ,3)

print(add(*t))
print(add(*"AD"))
print(add(*{1: 1, 2: 2}))

print("*************************")

print("-- **(dictionary unpacking) --")
# Definition: Unpacks the contents of a dictionary into a function call
# Syntax: function(**dict)
# -- dict: The dictionary containing pairs of keyword arguments and their values.
# Remarks:

# Example:
def add(a=0, b=0):
    return a + b

d = {'a': 2, 'b': 3}

print(add(**d))
print("*************************")

print("-- @(decorator) --")
# Definition: Returns a callable wrapped by another callable.
# Syntax: @decorator
#         def function():
#         decorator: A callable that takes another callable as an argument.
# Remarks:

# Decorator Syntax:
def decorator(f):
    pass

@decorator
def function():
    pass
# Is equivalent to:
def function():
    pass
function = decorator(function)

# Example:
print("*************************")

print(" -- ()(call operator --")
# Definition:
# Syntax:
# Remarks:

# Example:

print("*************************")
