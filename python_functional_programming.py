# Functional Programming
print("---= Functional Programming =---")

print("--= Map =--")
# Description: Applies function to every item of an iterable and returns a list of the results.
# Syntax: map(function,iterable[,...])
# -- function: Required. A function that is used to create a new list.
# -- iterable: Required. An iterable object or multiple comma-seperated iterable objects.
# Return Value: list
# Remarks: If additional iterable arguments are passed, function must take that many arguments and is applied
# -- to the items from all iterables in parallel.
# If one iterable shorter than another it is assumed to be extended with None items.
# If function is None, the identity function is assumed; if there are multiple arguments,
# -- map() returns a list consisting of tuples containing the corresponding items from all iterables.
# The iterable arguments may be a sequence or any iterable object; the result is always a list.

# Example:
l = map(lambda x, y, z: x+y+z, [1, 2, 3], [4, 5, 6], [7, 8, 9])
print(list(l))

def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

l = map(lambda x : x + x, numbers)
print(list(l))