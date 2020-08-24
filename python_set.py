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
# Description: Removes an element from the set.
# Syntax: set.discard(element)
# -- element: Required. The item you want to delete.
# Return Value: None

# Example:
s = {1, 2}
s.discard(1)
print(s)
print("-------------------------")

print("-- remove() --")
# Description: Removes an element from the set(raises KeyError if not found).
# Syntax: set.remove(element)
# Return Value: Required. The element you want to delete.

# Example:
s = {1, 2}
s.remove(2)
print(s)
print("-------------------------")

print("-- pop() --")
# Description: Removes and returns an arbitrary element from the set.
# Syntax: set.pop()
# Return Value: The same as deleted by calling this method.
# Remarks: Raises KeyError if the set is empty.

# Example:
s = {1, 2}
pop_val = s.pop()
print(pop_val)

print("-------------------------")

print("-- clear() --")
# Description: Removes all elements from the set.
# Syntax: set.clear()
# Return Value: None

# Example:
s = {1, 2}
s.clear()
print(s)
print("-------------------------")

print("--= Information =--")
print("-- issuperset() --")
# Description: Returns a Boolean stating whether the set contains the specified set or iterable
# Syntax: set.issuperset(iterable)
# -- iterable: Required. Iterable to be compared against the set.
# Return Value: bool
# Remarks: If the iterable is empty, returns True.

# Example:
s = {1, 2, 3}
bool = s.issuperset([2, 3])
print(bool)
print("-------------------------")

print("-- issubset() --")
# Description: Returns a Boolean stating whether the set is contained in the specified set or iterable.
# Syntax: set.issubset(iterable)
# -- iterable: Required. Iterable to be compared against the set.
# Return Value: bool
# Remarks: If the iterable is empty, returns False.

# Example:
s = {1}
s_1 = {'A', 'B', 'C'}
bool = s.issubset(s_1)
print(bool)
print("-------------------------")

print("-- isdisjoint() --")
# Description: Returns a Boolean stating whether the set contents overlap with the specified set or iterable.
# Syntax: set.isdisjoint(iterable)
# -- iterable: Required. Iterable to be compared against the set.
# Return Value: bool

# Example:
s = {0, 1, 2}
s_1 = {3, 4}
bool = s.isdisjoint(s_1)
print(bool)
print("-------------------------")

print("--= Set Operations =--")
print("-- difference() --")
# Description: Returns a new set with elements in the set that are not in the specified iterables.
# Syntax: set.difference(iterable, ...)
# -- iterable: Required. Iterable or multiple iterables to be compared against the set.
# Return Value: set

# Example:
s = {1, 2, 3, 4, 5, 6, 7}
s_1 = {4, 5, 6, 7, 8, 9, 10}

temp_s = s.difference(s_1)
print(temp_s)
print("-------------------------")

print("-- intersection() --")
# Description: Returns a new set with elements common to the set and the specified iterables.
# Syntax: set.intersection(iterable,...)
# -- iterable,...: Required. Iterable or multiple iterables to be compared against the set.
# Return Value: set

# Example:
s_1 = {2, 3}
s_2 = {2, 3, 4, 5}
s = {1, 2}.intersection(s_1, s_2)
print(s)
print("-------------------------")

print("-- symmetric_difference() --")
# Description: Returns a new set with elements in either the set or the specified iterable but not both.
# Syntax: set.symmetric_difference(iterable)
# -- iterable: Required. Any iterable
# Return Value: set

# Example:
s_1 = {2, 3}
s_2 = {2, 3, 4, 5}
s = s_1.symmetric_difference(s_2)
print(s)
print("-------------------------")

print("-- union() --")
# Description: Returns a new set with elements from the set and the specified iterables.
# Syntax: set.union(iterable,...)
# -- iterable: Required. Iterable or multiple iterables to be compared against the set.
# Return Value: set

# Example:
s_1 = {2, 3}
s_2 = {2, 3, 4, 5}
s = {1, 2}.union(s_1, s_2)
print(s)
print("-------------------------")

print("--= Set Operations Assignment =--")
print("-- difference_update() --")
# Description: Updates the set, removing elements found in others.
# Syntax: set.difference_update(iterable,...)
# -- iterable: Required. Iterable or multiple iterables to be compared against the set.
# Return Value: None.
# Time Complexity: O(len(t))

# Example:
s = {1, 2, 3, 4, 5}
s.difference_update({2, 3}, {4, 5})
print(s)
print("-------------------------")

print("-- intersection_update() --")
# Description: Updates the set, keeping only elements found in it and all others.
# Syntax: set.intersection_update(iterable,...)
# -- iterable: Required. Iterable or multiple iterables to be compared against the set.
# Return Value: None.

# Example:
s = {1, 2}
s.intersection_update({2, 3})
print(s)

s = {1, 2}
s.intersection_update({0, 1}, {1, 2})
print(s)
print("-------------------------")

print("-- symmetric_difference_update() --")
# Description: Updates the set, keeping only elements found in either set, but not in both.
# Syntax: set.symmetric_difference_update(iterable)
# -- iterable: Required. Any iterable.
# Return Value: None.
# Time Complexity: O(len(t)) to O(len(t) * len(s))

# Example:
s = {1, 2}
s.symmetric_difference_update({2, 3})
print(s)
print("-------------------------")

print("--= Copying =--")
print("-- copy() --")
# Description: Returns a copy of the set.
# Syntax: set.copy()
# Return Value: set

# Example:
s = {1, 2}
s_cpy = s.copy()
print(s_cpy)
print("-------------------------")

print("---= Set Operators =---")
print("--= Adding Elements =--")

print("-- |=(update) --")
# Description: Adds elements from another set.
# Syntax: set |= other
# -- other: A set object or expression evaluating to a set.
# Return Value: None.

# Example:
s = {0, 1}
s_1 = {1, 2}
s |= s_1
print(s)
print("-------------------------")

print("--= Relational Operators =--")
print("-- ==(is equal) --")
# Description: Returns a Boolean stating whether the set has the same elements as the other set.
# Syntax: set == other
# -- other: A set object or expression evaluating to a set
# Return Value: bool

# Example:
s = {0, 1}
s_1 = {1, 2}
is_false = s == s_1
print(is_false)
print("-------------------------")

print("-- !=(is not equal) --")
# Description: Returns a Boolean stating whether the set has different elements as the other set.
# Syntax: set != other
# -- other: A set object or expression evaluating to a set
# Return Value: bool

# Example:
s = {0, 1}
s_1 = {1, 2}
is_true = s != s_1
print(is_true)
print("-------------------------")

print("-- <=(issubset) --")
# Description: Returns a Boolean stating whether the set is contained in the other set.
# Syntax: set <= other
# -- other: A set object or expression evaluating to a set.
# Return Value: bool

# Example:
s = {0, 1}
s_1 = {0, 1, 2, 3, 4}
is_true = s.issubset(s_1)
print(is_true)
print("-------------------------")

print("-- <(issubset proper) --")
# Description: Returns a Boolean stating whether the set is contained in the specified set
# and that the sets are not equal.
# Syntax: set < other
# -- other: A set object or expression evaluating to a set.
# Return Value: bool

# Example:
is_true = {1, 2} < {1, 2, 3}
is_false = {1, 2} < {'frob'}

print(is_true)
print(is_false)
print("-------------------------")

print("-- >=(issuperset) --")
# Description: Returns a Boolean string whether the set contains the other set.
# Syntax: set >= other
# -- other: A set object or expression evaluating to a set.
# Return Value: bool

# Example:
s = {1, 2, 3}
s_1 = s.copy()
s_2 = {4, 5, 6}

is_true = s >= s_1
is_false = s >= s_2

print(is_true)
print(is_false)
print("-------------------------")

print("-- >(issuperset proper) --")
# Description: Returns a Boolean string whether the set contains the other set and that the sets are not equal.
# Syntax: set > other
# -- other: A set object or expression evaluating to a set.
# Return Value: bool

# Example:
s = {0, 1, 2, 3}
s_1 = {1, 2, 3}

is_true = s > s_1
print(is_true)
print("-------------------------")

print("--= Set Operations =--")
print("** -(difference) **")
# Description: Returns a new set with elements in the set that are not in the other set.
# Syntax: set - other
# -- other: A set object or expression evaluating to a set.
# Return Value: set
# Time Complexity: O(len(s))

# Example:
s = {1, 2, 3, 4}
s_1 = {5, 6, 7, 8}
s_2 = {4, 5, 6, 7}

new_s = s - s_1 - s_2
print(new_s)
print("-------------------------")

print("-- &(intersection) --")
# Description: Returns a new set with elements common to the set and the other set.
# Syntax: set & other
# -- other: A set object or expression evaluating to a set.
# Return Value: set
# Time Complexity: O(min(len(s), len(t)) to O(len(s)*len(t))

# Example:
s_1 = {5, 6, 7, 8}
s_2 = {4, 5, 6, 7}

new_s = s_1 & s_2
print(new_s)
print("-------------------------")

print("-- ^(symmetric difference) --")
# Description: Returns a new set with elements in either the set or the other set but not both.
# Syntax: set ^ other
# other: A set object or expression evaluating to a set.
# Return Value: set
# Time Complexity: O(len(s)) to O(len(s)*len(t))

# Example:
s_1 = {5, 6, 7, 8}
s_2 = {4, 5, 6, 7}

new_s = s_1 ^ s_2
print(new_s)
print("-------------------------")

print("-- |(union) --")
# Description: Returns a new set with elements from the set and the other set.
# Syntax: set | other
# -- other: A set object or expression evaluating to a set.
# Return Value: set
# Time Complexity: O(len(s) + len(t))

# Example:
s = {1, 2}
s_1 = {3, 4}
s_2 = {4, 5}

new_s = s | s_1 | s_2
print(new_s)
print("-------------------------")

print("--= Set Operations Assignment =--")
print("** -=(difference_update) **")
# Description: Updates the set, removing elements found in the other set.
# Syntax: set -= other |...
# -- other: A set object or expression evaluating to a set.
# Return Value: set

# Example:
s = {1, 2}
s -= {2, 3}
print(s)
print("-------------------------")

print("-- &=(intersection_update) --")
# Description: Updates the set, keeping only elements found in it and the other set.
# Syntax: set &= other & ...
# -- other: A set object or expression evaluating to a set.
# Return Value: set

# Example:
s = {1, 2}
s &= {2, 3}
print(s)
print("-------------------------")

print("-- ^=(symmetric_difference_update) --")
# Description: Updates the set, keeping only elements found in either the set or the other set, but not in both.
# Syntax: set ^= other
# -- other: A set object or expression evaluating to a set.
# Return Value: set

# Example:
s = {1, 2, 3, 4, 5}
s ^= {3, 4, 5, 6, 7}
print(s)
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

