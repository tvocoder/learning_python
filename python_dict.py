# dict
# mutable unordered collections of key-value pairs.
# -- keys: must be unique and hashable
# -- includes types like numbers, strings, and tuples.
# -- list and dicts can not be used as keys since they are mutable.
# -- also known as hash tables or associative arrays

print("---=Constructors=---")
# Constructors

## dict(): returns a dictionary object
# Syntax: dict([**kwargs])
#         dict([mapping, **kwargs])
#         dict([iterable, **kwargs])
# -- kwargs: Optional. Keyword arguments.
# -- mapping: Optional. Another dictionary.
# -- iterable: Optional. An iterable object in a form of key-vale pair(s).
# Return Value: dict()
# Remarks: If no positional argument is given an empty dictionary is created. If a positional argument is given and it
# -- a mapping object, a dictionary is created with the same key-value pairs as the mapping object.
# -- Otherwise, the positional argument must be an iterable object. Each item in the iterable must be itself be an
# -- iterable object. Each item in the iterable itself must be an iterable with exactly two objects.
# -- The first object of each item becomes a key in the new dictionary, and the second object the corresponding value.
# -- If a key occurs more than once, the last value for that key becomes the corresponding value in the new dictionary.
#
# -- If keyword arguemnts are given, the keyword arguments and their values are added to the dictionary created from
# -- the positional argument. If a key being added is already present, the value from the keyword argument repaces the
# -- value from the positional argument.

# Example
print("--dict()--")

dict1 = dict(a=1, b=2)
dict2 = dict([('a', 1), ['b', 2]], c=3)
print(dict2)

print("********************")

## {} dictionary comprehension
# Description: Returns a dictionary based on existing iterables.
# Syntax: {expression(variable): expression(variable) for variable, variable in input_set[predicate][,...]}
# -- expression: Optional. An output expression producing members of the new set from members of the input set that
# --- satisfy the predicate expression.
# -- variable: Required. Variables representing members of an input set.
# -- input_set: Required. Represents the input set.
# -- predicate: Optional. Expression acting as a filter on members of the input set.
# -- [,...]]: Optional. Another nested comprehension.
# Return Value: dict

# Example
print("--{}--")

dict_compr = {k: v for k, v in [(1, 2), (3, 4)]}
print(dict_compr)

dict_compr = {chr(n): n for n in (65, 66, 66)}
print(dict_compr)

dict_compr = {k: v for k, v in (('a', 0), ('b', 1)) if v == 1}
print(dict_compr)

print("********************")

## Literal Syntax
# -- Dictionaries can be initialized by enclosing comma separated colon delimited key:value pairs in
# -- squiggly brackets {}. Keys within the dict must be unique. Dictionaries do not maintain the items order.

# Example
print("--Literal Syntax--")

d = {'A': 1, 'B': 2}
print(d)

print("********************")


## Methods
print("---=Methods=---")

print("---Content Access---")
# Content Access

# get(): returns the value for key in dictionary; if not found returns default value.
# Syntax: dict.get(key[,default])
# -- key: Required. A key in the dictionary.
# -- default: Optional. Value that is returned when the key is not found. Defaults to None, so that this method
# --- never raises a KeyError.
# Return Value: The value of the key.

# Example:
print("--.get()--")
d = {'a': 1, 'b': 2}
key_cpy = d.get('a')
print(key_cpy)

print(d.get('x', 'Not found'))

# items(): returns a copy of the dictionary's list of (key,value) pairs.
# Syntax: dict.items()
# Return Value: list
# Remarks: If items(), keys(), values(), iteritems(), iterkeys(), and itervalues() are called with no intervening
# -- modifications to the dictionary, the lists will directly correspond. This allows the creation of (key,value)
# --- pairs using zip():

# Example -- zip():
print("--.zip()--")
d = {'a': 1, 'b': 2, 'c': 3}
pairs = zip(d.values(), d.keys())
print(pairs)

# Example -- items()
print("--.items()--")
d_items = d.items()
print(d_items)

print("********************")

# keys(): returns a copy of the dictionary's list of keys.
# Syntax: dict.keys()
# Return Value: list

# Example:
print("--.keys()--")
d = {'a': 1, 'b': 2, 'c': 3}
print(d.keys())

print("********************")

# values(): returns a copy of the dictionary's list of values.
# Syntax: dict.values()
# Return Value: list

# Example:
print("--.values()--")
d = {'a': 1, 'b': 2, 'c': 3}
print(d.values())

print("********************")

print("---Adding Elements---")
# Adding Elements

# update(): adds key:value pairs to the dictionary.
# Syntax: dict.update([mapping])
# mapping: Required. Either another dictionary object or an iterable of key:value pairs
# -- (iterables of length two). If keyword arguments are specified, the dictionary is then updated with those
# -- key:value pairs
# Return Value: None

# Examples:
print("--.update()--")
d = {'a': 1, 'b': 2, 'c': 3}
d.update({'a': 'I', 'c': 3})
print(d)

d = {'a': 1, 'b': 2, 'c': 3}
d.update([('x', 10), ('y', 20)])
print(d)

d = {'a': 1, 'b': 2, 'c': 3}
d.update(foo='bar', sn='afu')
print(d)
print("********************")

print("--Deleting--")
# Deleting

# clear(): removes all items from the dictionary
# Description: Removes all items from the dictionary.
# Return Value: None

# Example(s):
print("--.clear()--")

d_2 = {'a': 1, 'b': 2, 'c': 3}
print(d_2.clear())
print("********************")

# pop(): removes the key in the dictionary and returns its value
# Syntax: dict.pop(key[,default])
# -- key: Required. A dictionary key.
# -- default: Optional. Default value to be returned if key is not found.
# Return Value: The same as deleted item.
# Remarks: If default is not given and key is not in the dictionary, a KeyError is raised.

# Examples:
print("--.pop()--")

d_3 = {'a': 1, 'b': 2, 'c': 3}
pop_corn = d_3.pop('c', "Not Found")
print(pop_corn)
pop_corn = d_3.pop('d', "Not Found")
print(pop_corn)

print("********************")

# popitem(): removes and returns an arbitrary key:value pair from dict
# Syntax: dict.popitem()
# Return Value: tuple
# Remarks: useful to destructively iterate over a dictionary, as often used in 'set' algorithms. If the dictionary
# -- is empty, calling popitem() raises a KeyError.

# Example:
print("--.popitem()--")

d_4 = {'a': 1, 'b': 2, 'c': 3}
t = d_4.popitem()
print(t)

print("********************")

print("---Information---")
## Information

# has_key(): Returns a Boolean stating whether the specified key is in the dictionary.
# Syntax: dict.has_key(key)
# -- key: Required. The key you are looking for.
# Return: **bool*
# Note: has_key() is depricated in favor of key in d.

# Example:
print("--.has_key()--")

d_5 = {'a': 1, 'b': 2, 'c': 3}

# recommended instead
print("best practice: ")

is_true = 'a' in d_5
print(is_true)
print("********************")

print("---Other---")
## Other

# copy(): returns a shallow copy of the dictionary

# Syntax: dict.copy()
print("--dict.copy()--")
# Example:

d = {'a': 1, 'b': [1, 2]}
dd = d.copy()
print(dd)

d['b'][0] = 'foo'   # since copy() returns a shallow copy
print(dd)           # (only references to the copied elements are returned),
                    # Altering the objects in original dictionary will affect it's copy as well.
print("********************")

# fromkeys(): returns a new dictionary with keys from iterable and values all set to a specified value.
# -- deep copy
# Syntax: dict.fromkeys(iterable[,value])
# -- iterable: Required. Any iterable.
# -- value: Optional. Default value for the keys. Default value is None.
# Return Value: dict
print("--dict.fromkeys()--")
# Example:
l = [1, 2, 3]
d = {}
print(d.fromkeys(l))

d = {}.fromkeys([1, 2, 3], "NULL")
print(d)
print("********************")

print("---Iterators---")
## Iterators

# iteritems(): returns an iterator over the dictionary's key:value pairs.
# Syntax: dict.iteritems()
# Return Value: iterator
# Remarks: Using iteritems() while adding or deleting entries in the dictionary may raise a Runtime Error
# -- or fail to iterate over all entries
# https://python-reference.readthedocs.io/en/latest/docs/dict/index.html
print("********************")

# itervalues(): returns an iterator over the dictionary's values.
# Syntax: dict.itervalues()
# Return: iterator
# Remarks: Using itervalues() while adding or deleting entries in the dictionary may raise a RuntimeError or fail
# -- to iterate overall entries


# iterkeys(): returns an interator over the dictionary's keys.
print("********************")

print("---Dictionary Views---")
## Dictionary Views

# viewitems(): Returns a new view of the dictionary's items ((key,value) pairs).
# Syntax: dict.viewitems()
# Return Value: dict_items Object
# Remarks: Objects returned by dict.viewkeys(), dict.viewvalues(), and dict.viewitems() are view objects.
# -- They provide a dynamic view on the dictionary's entries, which means that when the dictionary changes, the view
# -- reflects these changes.
print("********************")

# viewvalues()
print("********************")

# viewkeys()
print("********************")

print("---Dictionary View Operators---")
## Dictionary View Operators

# &(itersection): returns elements that appear both in the dictview and the specified iterable.
print("********************")


# ^(symnmetric difference): returns elements that appear in either the dictview or the specified iterable, but not both
print("********************")


# -(difference): returns elements that appear in the dictview and not in the specified iterable.
print("********************")


# |(union): returns elements that appear in the dictview and the specified iterable.

print("********************")

print("---=Functions=---")
## Functions

# len(): returns an into type specifying number of elements in the collection.
# Syntax: len (collection)
# -- collection: Required. Must be a sequence type.

print("--len()--")
# Example

print(len('foo'))

print("********************")

# min(): returns the smallest item from a collection.
# Syntax: min(collection[,key])
# -- collection: Required. A comma-separated list of objects or an iterable sequence.
# -- key: Optional. Specifies a one-argument ordering function; must be in keyword form.

print("--min()--")
# Example
func = min('apple', 'pear', key=lambda x: x.upper())
print(func)
print("********************")

# max(): returns largest item in an iterable or largest of two or more arguments.
# Syntax: max(collection[,key])
# -- collection: Required. A comma-separated list of objects or an iterable sequence.
# -- key: Optional. Specifies a one-argument ordering function; must be in keyword form.

print("--max()--")
# Example:

func_1 = max('2', '1', key=lambda val: val.isdigit())
print(func_1)
print("********************")

# sum(): returns a total of the items contained in the iterable object.
# Syntax: sum(iterable[,start])
# -- iterable: Required. An iterable object.
# -- start: Optional. An integer specifying the start value.
# Remarks: For some use cases, there are good alternatives to sum().
# -- Fast way to concatenate a sequence of strings is by calling
# ---- "".join(sequence).
# -- To add floating point values with extended precision, see
# ---- math.fsum()
# -- To concatenate a series of iterables, considering using
# ---- itertools.chain()

print("--sum()--")
# Example:
val = sum({1, 2, 3}, 10)
print(val)

val_1 = sum({1: 'a', 2: 'b', 3: 'c'}, 10)
print(val_1)
print("********************")

# sorted(): returns a sorted list from the iterable.
# Syntax: sorted(iterable[,cmp[,key[,reverse]]])
# iterable: Required.
# cmp: Optional. A custom comparison fuction of two arguments(iterable elements) which should return a negative,
# -- zero or positive number depending on whether the first argument is considered smaller than, equal to, or larger
# -- than the second argument. The default value is None.
# key: Optional. A function of one argument that is used to extract a comparison key from each list element. The
# -- default value is None(compare the elements directly).
# reverse: Optional. Boolean value. If set to True, then the list elements are sorted as if each comparison were
# -- reversed.
# Remarks: The key and the reverse conversion processes are much faster than specifying an equivalent cmp function.
# -- This is because cmp is called multiple times for each list element which key and reverse touch each element only
# -- once. Use functools.cmp_to_key() to convert an old-style cmp function to a key function.

print("--sorted()--")
# Example
sorted_1 = sorted({'a': 1, 'b': 2, 'c': 3})
print(sorted_1)

sorted_2 = sorted('foobar', reverse = True)
print(sorted_2)

sorted_3 = sorted(((9, ), (1, 2, 3), (1, 2)), key = lambda val: sum(val))
print(sorted_3)

print("********************")

# reversed(): reverse iterator over a sequence.
# Syntax: reversed(sequence)
# -- sequence: Required. Any iterable sequence.
# Remarks: Sequence must be an object with has a __reversed__() method or supports the sequence protocol
# --- (the __len()__ method and the __getitem__() method with integer arguments starting at 0)

print("--reversed()--")
# Example:

r = reversed([1, 2, 3, 4])
print(*r)

for r in reversed((1, 2, 3, 4)):
    print(r)
print("********************")

# all(): returns a Boolean value that indicates whether the collection contains any values that evaluates to True.
# Syntax: all(iterable)
# -- iterable: Required. Any iterable type.
# Remarks: If the iterable is empty, all() returns True.

print("--all()--")
# Example:

it = []
print(all(it))

it_1 = {0: 'zero', 1: 'one'}
print(all(it_1))
print("********************")

# any(): Returns a Boolean value that indicates whether the collection contains any values that evaluate to True.
# -- iterable: Required. Any iterable type.
# Remarks: If the iterable is empty, returns False.

print("--any()--")
# Example:

it = []
print(any(it))

it_1 = {0: 'zero', 1: 'one'}
print(any(it_1))

print("********************")

# enumerate(): returns an enumerate object.
# Syntax: enumerate(sequence, start=0)
# -- sequence: Required. Must be a sequence, an iterator, or some other object which supports iteration.
# -- start: Optional. Index at which enumeration starts.
# Remarks: The next() method of the iterator returned by enumerate() returns a tuple containing a count
# -- (from start which defaults to 0) and the values obtained from iterating over sequence.

print("--enumerate()--")
# Example:

for it in enumerate ((1, 2, 3)):
    print(it)

# e = enumerate([1, 2, 3], 1)
# e = enumerate([1, 2, 3], start=1)
# e.next()
# e.next()
# e.next()

print("********************")

print("--zip()--")
# zip(): returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument iterables
# Syntax: zip([iterable, ...]
# iterable: Optional. An iterable object.
# Remarks: Returned list is truncated in length to the length of the shortest argument sequence. When there are
# -- multiple arguments which are all of the same length, zip() is similar to map() with an initial argument of None.

# -- With a single sequence argument, it returns a list of 1-tuples. With no arguments, it returns an empty list.
# -- The left-to-right evaluation order of the iterables is guaranteed. This makes possible an idiom for clustering a
# -- data series into n-length groups using zip(*[iter(s)*n)

# Example:
# -- zip() in conjunction with the * operator can be used to unzip a list:
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(*zipped)

# x2, y2 = zip(*zipped)
# is_true = x == list(x2) and y == list(y2)

zipped = zip((1, 2, 3), (4, 5))
print(*zipped)
print("********************")

print("---Misc---")
## Misc

# [] (key lookup): Returns the value associated with the given key.
# Syntax: dict[key]
# -- key: Required. Key which value is to be retrieved.
# Return Value: The same as associated with key.

print("--dict[key]--")
# Example:
d = {'a': 1, 'b': 2}['a']
print(d)
print("********************" )