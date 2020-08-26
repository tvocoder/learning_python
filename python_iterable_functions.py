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

for it in enumerate((1, 2, 3)):
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
print(list(zipped))
print(*zipped)

# x2, y2 = zip(*zipped)
# is_true = x == list(x2) and y == list(y2)

zipped = zip((1, 2, 3), (4, 5))
print(*zipped)
print("********************")
