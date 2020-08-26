print("---= Callables Operators =---")

print("-- *(tuple packing) --")
# Description: Packs the consecutive function positional arguments into a tuple.
# Syntax: def function(*tuple): '
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
# Definition:
# Syntax:
# Remarks:

# Example:

print("*************************")

print("-- *(tuple unpacking) --")
# Definition:
# Syntax:
# Remarks:

# Example:

print("*************************")

print("-- **(dictionary unpacking) --")
# Definition:
# Syntax:
# Remarks:

# Example:

print("*************************")

print("-- @(decorator) --")
# Definition:
# Syntax:
# Remarks:

# Example:

print("*************************")

print(" -- ()(call operator --")
# Definition:
# Syntax:
# Remarks:

# Example:

print("*************************")
