# Lists are mutable ordered and indexed collections of objects.
# The items of a list are arbitrary Python Objects.
# Lists are formed by placing comma-separated list of expressions in square brackets.
# (Note that there are no special cases needed to for lists of length 0 or 1)

print("---= Constructors =---")
print("-- list() --")
# Description: Converts an object into a list.
# Syntax: list([iterable])
# Return Value: list
# Remarks: Returns a list whose items are the same and in the same order as iterable's items.
# Iterable may be either a sequence, a container that supports iteration, or an iterator object.
# If iterable is already a list, a copy is made and returned, similar to iterable[:]

# Example:
l = iter([1, 2])
print(l)
print(*l)
print("-------------------------")

print("-- [] List Comprehensions --")
# Description: Returns a list based on existing iterables.
# Syntax: [expression(variable) for variable in input_set [predicate][,...]]
# -- expression: Optional. An output expression producing members of the new set from members of the input set that
# satisfy the predicate expression.
# -- variable: Required. Variable representing members of an input set.
# -- input_set: Required. Represents the input set.
# -- predicate: Optional. Expression acting as a filter on members of the input set.
# -- [,...]]: Optional. Another nested comprehension.
# Return Value: list
# Remarks: A list comprehension follows the form of the mathematical set-builder notation(set comprehensions) as
# distinct from the use of map() and filter() functions.

# Example:
l = [2 * n for n in (0, 1, 2) if n > 0]
# l = list of all numbers 2 * n where n is an item in the (0, 1, 2) tuple, for which tuple element is greater than 0.
print(l)

l = [n for n in [1, 2, 3]]
print(l)

# squared
l = [n**2 for n in range(10)]
print(l)

# odd numbers only
l = [n for n in [1, 2, 3] if n % 2 == 1]
print(l)

# cross product
l = [[m,n] for n in [i for i in [0, 1]] for m in [1, 2]]
print(l)
print("-------------------------")

print("-- Literal Syntax --")
# Description: List can be initialized separating enclosing comma separated values in square brackets [].

# Example:
a = 'AA'
b = 'BB'
l = [a, b]

print(l)
print("-------------------------")

print("---= Methods =---")
print("--= Adding Elements =--")

print("-- insert() --")
# Description: Inserts an item at a given position.
# Syntax: list.insert(index, object)
# -- index: Required. The index of the element before which to insert.
# -- object: Required. The item to insert.
# Return Value: None.
# Time Complexity: O(n)

# Example:
l = [1, 2]
l.insert(0, 0)

print(l)
print("-------------------------")

print("-- append() --")
# Description: Adds an item to the end of the list.
# Syntax: list.append(object)
# -- object: Required. Any valid type.
# Return Value: None.
# Time Complexity: O(1)

# Example:
l = [1, 2]
l.append(3)

print(l)
print("-------------------------")

print("-- extend() --")
# Description: Extends the list by appending all the items from the iterable.
# Syntax: list.extend(iterable)
# -- iterable: Required. Any iterable type.
# Return Value: None.
# Time Complexity: O(k)

# Example:
l = [1, 2]
l.extend([3, 4])
l.extend('foo')
l.extend((5, 6))
l.extend({'x': 100, 'y': 200})

print(l)
print("-------------------------")

print("--= Deleting =--")
print("-- remove() --")
# Description: Removes the first item from the list which matches the specified value.
# Syntax: list.remove(object)
# -- object: Required. Any valid type. If not found error is raised.
# Return Value: None

# Example:
l = [1, 2]
l.remove(2)

print(l)
print("-------------------------")

print("-- pop() --")
# Description: Removes and returns the item at the specified index.
# Syntax: list.pop([index])
# -- index: Optional. Index of the item you want to delete. Default value is -1 (the last item in the list)
# Return Value: Deleted Value
# Time Complexity: O(1) for pop(); O(n) for pop(index)

# Example:
l = [1, 2, 3]
val = l.pop()

print(val)
print("-------------------------")

print("--= Information =--")
print("-- index() --")
# Description: Returns the index of the first occurrence of the specified list item.
# Syntax: list.index(item)
# -- item: Required. Any valid type. ValueError is raised if item is not in the list.
# Return Value: int
# Time Complexity: O(1)

# Example:
l = [1, 2, 3]

print(l.index(2))
print("-------------------------")

print("-- count() --")
# Description: Returns the number of times the specified item appears in the list.
# Syntax: list.count(item)
# -- item: Required. Any valid type.
# Return Value: int

# Example:
l = [1, 2, 3, 1, 1, 1, 1]
cnt = l.count(1)

print(cnt)
print("-------------------------")

print("--= Modifying =--")
print("-- sort() --")
# Description: Sorts the list in place.
# Syntax: list.sort([cmp[,key[,reverse]]])
# -- cmp: Optional. Specifies a custom comparison function of two arguments (list items) which should return
# a negative, zero, or positive number depending on whether the first argument is considered smaller than, equal to,
# or larger than the second argument: The default value is None.
# -- key: Optional. Specifies a function of one argument that is used to extract a comparison key
# from each list element. The default value is None.
# -- reverse: Optional. A boolean value. If set is True, then the list elements are sorted as if each comparison were
# reversed.
# Return Value: None.
# Time Complexity: O(n log n)
# Remarks: In general, the key and reverse conversion processes are much faster than specifying an equivalent
# cmp function. This is because cmp is called multiple times for each list element while key and reverse touch
# each element only once.

# Example:
l = [1, 3, 2]
l.sort()
print(l)

l = ['A', 'B', 'a', 'c']
l.sort(key=lambda x: x.lower())
print(l)

l.sort(key=lambda x: x.lower(), reverse=True)
print(l)
print("-------------------------")

print("-- reverse() --")
# Description: Reverses the elements of the list, in place.
# Syntax: list.reverse()
# Return Value: None
# Time Complexity: O(n)

# Example:
l = [1, 2, 3]
l.reverse()

print(l)
print("-------------------------")

print("---= Functions =---")

print("-- cmp() --")
# Description:
# Syntax:
# Return Value:
# Remarks:

# Example:
print("-------------------------")

print("---= Operators =---")

print("-- [](index operator) --")
# Description: Gives access to a sequence's element.
# Syntax: sequence[index]
# -- index: Index of the item you want to access. Must be an integer.
# Return Value: The same as selected.
# Time Complexity: O(1)
# Discussion: The built-in fundamental sequence types are:
# -- strings - str and unicode
# -- arrays - list and tuple
# Since all sequences are ordered and indexed arrays of objects, each object stored in a sequence has it's associated
# index number - positive one, zero indexed and starting from left, and -1 from the right.

# Example:
l = ([0, 1], [2, 3])
val = l[0][0]
print(val)

l = [0, 1, 2, 3, 4]
print(l[-1])
# since lists are mutable indexes can be used for item assignment or deletion
l[-1] = "ABCD"
print(l)
print("-------------------------")

print("-- [:](slicing) --")
# Description: Gives access to a specified range of sequence's elements
# Syntax: [start:stop[:step]]
# -- start: Optional. Starting index of the slice. Defaults to 0.
# -- stop: Optional. The last index of the slice or the number of items to get. Defaults to len(sequence).
# -- step: Optional. Extended slice syntax. Step value of the slice. Defaults to 1.
# Return Value: The same as selected.
# Time Complexity: O(k) for slice retrieval; O(n) for deletion; O(n+k) for slice assignment

# Example:
val = "ABCD"[0:4:2]
print(val)

# Negative step argument can be used to reverse the sequence:
val = "ABCD"[::-1]
print(val)

# Slices can be used to replace multiple items.
l = [0, 1, 2, 3]
l[:2] = ("AB", "CD")
print(l)

# deleting items
l = [0, 1, 2, 3]
del l[::2]
print(l)
print("-------------------------")

print("-- +(concatention) --")
# Description: Returns a concatenation of two sequences.
# Syntax: A + B
# -- A: Any sequence.
# -- B: Sequence of the same type as A.
# Return Value: The same as used as sequence operands.
# Time Complexity: O(k)

# Example:
print("AB" + "CD")
print((1, 2, 3) + (4, 5, 6))
print("-------------------------")

print("-- *(multiple concatenation) --")
# Description: Returns a sequence self-concatenated specified amount of times.
# Syntax: A * N or N * A
# -- A: Any sequence
# -- N: Any expression evaluating to a numeric type.
# Return Value: The same as used as sequence operand.
# Time Complexity: O(nk)

# Example:
print("A" * 10)
print([0, 1] * 2)
print("-------------------------")