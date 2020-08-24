# Sets are mutable unordered collections of unique elements.
# Common uses include membership testing, removing duplicates from a sequence, and computing standard math operations
# -- sets such as intersection, union,  difference, and symettric difference.

# Sets do not record element position of insertion. Accordingly, sets do not support indexing, slicing, or other
# -- sequence-like behavior

# Sets are implemented using dictionaries. They cannot contain mutable elements such as lists or dictionaries.
# -- However, they can contain immutable collections.

print("---= Constructors =---")

print("--- set() ---")
# Description: Returns a set type initialized from iterable.
# Syntax: set([iterable])
# -- iterable: Required. All of the elements in iterable should be immutable.
# Return Value: set
# Remarks: Set is an unordered, mutable collection of unique elements. See frozenset() for the immutable version.

# Example:
s = set([1, 2, 2])
print(s)

s_1 = set({'a': 1, 'b': 2})
print(s_1)

s_3 = set('foo')
print(s_3)
print("-------------------------")

print("--- {} set comprehension ---")
# Description: Returns a set based on existing iterables.
# Syntax: {expression(variable) for variable in input_set[predicate][,...]}
# -- expression: Optional. An output expression producing members of the new set from members of the input set
# from members of the input set that satisfy the predicate expression.
# -- variable: Required. Variable representing members of an input set.
# -- input_set: Required. Represents the input set.
# -- predicate: Optional. Expression acting as a filter on members of the input set.
# -- [,...]]: Optional. Another nested comprehension.
# Return Value: set

# Example:
s = {s for s in [1, 2, 1, 0]}
print(s)

s_1 = {s ** 2 for s in range(10)}
print(s_1)

s_2 = {s for s in [1, 2, 3] if s % 2}
print(s_2)

s_3 = {(m, n) for n in range(2) for m in range(3, 5)}
print(s_3)
print("-------------------------")

print("--- literal syntax ---")

s = {True, 3.14, "ABC"}
print(s)
print("-------------------------")

print("---= Methods =---")
print("--= Adding Elements =--")

print("-- add() --")
# Description: Adds an element to the set.
# Syntax: set.add(element)
# -- element: Required. Element to be added to the set. Must be of a hashable type.
# Return Value: None.

# Example:
s = {1, 2}
s.add(3)
print(s)

# TypeError:
# s = {1, 2}
# s.add({3, 4}) -- TypeError: unhashable type: 'set'
# {} unhashable type: 'set'
# [] unhashable type: 'list'
# {'a': 1} unhashable type: 'dict"

print("-- update() --")
# Description: Adds elements to the set.
# Syntax: set.update(other,...)
# -- other,...: Required. Iterable or multiple iterables which elements are to be added to the set.
# The elements must be hashable.
# Return Value: None.

# Example:
s = {1, 2}
s.update({3, 4}, [5, 6])
print(s)
print("-------------------------")

print("--= Deleting =--")
print("-- discard() --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- remove() --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- pop() --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- clear() --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")

print("--= Information =--")
print("-- issuperset() --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- issubset() --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- isdisjoint() --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")

print("--= Set Operations =--")
print("-- difference() --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- intersection() --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- symmetric_difference() --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- union() --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")

print("--= Set Operations Assignment =--")
print("-- difference_update() --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- intersection_update() --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- symmetric_difference_update() --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")

print("--= Copying =--")
print("-- copy() --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("---= Set Operators =---")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("--= Adding Elements =--")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- |=(update) --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")

print("--= Relational Operators =--")
print("-- ==(is equal) --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- !=(is not equal) --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- <=(issubset) --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- <(issubset proper) --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- >=(issuperset) --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- >(issuperset proper) --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")

print("--= Set Operations =--")
print("** -(difference) **")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- &(intersection) --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- ^(symmetric difference) --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- |(union) --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")

print("--= Set Operations Assignment =--")
print("** -=(difference_update) **")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- &=(intersection_update) --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")
print("-- ^=(symmetric_difference_update) --")
# Description:
# Syntax:
# Return Value:

# Example:
print("-------------------------")

print("---= Functions =---")
print("-- len() --")
print("-- min() --")
print("-- max() --")
print("-- sum() --")
print("-- sorted() --")
print("-- reversed() --")
print("-- all() --")
print("-- any() --")
print("-- enumerate() --")
print("-- zip() --")

