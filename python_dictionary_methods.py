# w3schools.com
# amazon.com
# geeksforgeeks.com

# import copy module
# used for shallow and deep copy operations.
# import copy

# dictionary
book = {
    "Title": "Elements: A Visual Exploration of Every Known Atom in the Universe",
    "Publisher": "Black Dog & Leventhal",
    "Languages": ["English"],
    "Pages": 240,
    "ISBN10": "9781579128142"
}

# accessing items.
# refer to its key name, inside square brackets.
isbn_value = book["ISBN10"]
print(isbn_value)

# accessing items. alternative version.
# .get()
pages_value = book.get("Pages")
print(pages_value)

# change values
# by referring to its key name.
book["Languages"] = ["Vietnamese"]
print(book)

# looping through a dictionary
# the return value are the 'keys' of the dictionary

# for loop -- keys(k)
for k in book:
    print(k)

# for loop -- values(v)
for v in book:
    print(book[v])

# for loop -- keys() method -- returns keys(k)
for k in book.keys():
    print(k)

# for loop -- values() method -- returns value(v)
for v in book.values():
    print(v)

# for loop -- items() method -- returns both keys and their values
for k, v in book.items():
    print(k, v)

# adding items to dictionary
# -- new index key -- assigning a value to it
book["ISBN13"] = "978-1579128142"
print(book)
print("-------------")

# dict() Constructor
book_cpy = dict(book)
print(book_cpy)
print("-------------")

# copy() -- Returns a copy of the dictionary
book_cpy = book.copy()
print(book_cpy)
print("-------------")

# popitem() -- Removes the last inserted key-value pair
removed_key_value = book_cpy.popitem()
# removed_property holds key-value pair removed
print(removed_key_value)
# print book_cpy with last key-value paired removed
print(book_cpy)

# dict() -- Make a copy of a dictionary
book_cpy_2 = dict(book_cpy)
print(book_cpy_2)
print("-------------")

# dict() Constructor
new_book = dict(Title = "Algebra 1, Common Core Edition", Publisher = "McGraw-Hill Education", Language = ["English"], Pages = 1040, ISBN10 = "0076639231")
print(new_book)
print("-------------")

# Nested Dictionaries
library = {
    # storing three books into a library dictionary
    "book1": book,
    "book2": book_cpy,
    "book3": book_cpy_2,
    "book4": new_book
}
print(library)
print("-------------")

# del (keyword) removes item with the specified key name.
del library["book3"]
print(library)
del library["book2"]
print(library)
print("-------------")

# copy() -- Returns a copy of the dictionary
new_library = library.copy()

# Removing Items
# pop() removes the item with the specified key name.
removed_book = library.pop("book4")
print(removed_book)
print("-------------")

removed_book_2 = library.pop("book1")
print(removed_book_2)
print("-------------")

# clear() -- Removes all the elements from the dictionary
library.clear()
print(library)
print("-------------")

# fromkeys(keys, value) -- Returns a dictionary with specified keys and value
# -- keys -- Required. An iterable specifying the keys of the new dictionary
# -- value -- Optional -- The value for all keys. Default value is None
library_keys = ('book_1', 'book_2')
library_values = (removed_book, removed_book_2)

new_library = dict.fromkeys(library_keys, library_values)
print(new_library)
print("-------------")

# dictionary.get(keyname, value)
# -- keyname -- Required. The keyname of the item you want to return the value from.
# -- value -- Optional. -- A value to return if the specified key does not exist. Default None
prop_none = new_library.get("Price", "Freedom")
print(prop_none)
print("-------------")

# methods:
# update(): Updates the dictionary with the specified key-value pairs.
# fromkeys(): Returns a dictionary with specified keys and value
# get(): Returns the value of the specified key
# items(): Returns a list containing a tuple for each key value pair
# keys(): Returns a list containing the dictionary's keys
# pop(): Removes the element with the specified key
# setdefault(): Returns the value of the specified key. If the key does not exist:
    # Insert the key, with the specified value.
# values(): Returns a list of all the values in the dictionary.
# clear(): Removes all the elements from the dictionary
