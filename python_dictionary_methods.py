# w3schools.com
# amazon.com
# geeksforgeeks.com

# import copy module
# used for shallow and deep copy operations.
# import copy

# dictionary
books = {
    "Publisher": "Black Dog & Leventhal",
    "Languages": ["English"],
    "Pages": 240,
    "ISBN-10": "9781579128142"
}

# accessing items.
# refer to its key name, inside square brackets.
isbn_value = books["ISBN-10"]
print(isbn_value)

# accessing items. alternative version.
# .get()
pages_value = books.get("Pages")
print(pages_value)

# change values
# by referring to its key name.
books["Languages"] = "Vietnamese"
print(books)

# looping through a dictionary
# the return value are the 'keys' of the dictionary

# for loop -- keys(k)
for k in books:
    print(k)

# for loop -- values(v)
for v in books:
    print(books[v])

# for loop -- keys() method -- returns keys(k)
for k in books.keys():
    print(k)

# for loop -- values() method -- returns value(v)
for v in books.values():
    print(v)

# for loop -- items() method -- returns both keys and their values
for k, v in books.items():
    print(k, v)





# methods:
# copy(): Returns a copy of the dictionary
# update(): Updates the dictionary with the specified key-value pairs.
# fromkeys(): Returns a dictionary with specified keys and value
# get(): Returns the value of the specified key
# items(): Returns a list containing a tuple for each key value pair
# keys(): Returns a list containing the dictionary's keys
# pop(): Removes the element with the specified key
# popitem(): Removes the last inserted key-value pair
# setdefault(): Returns the value of the specified key. If the key does not exist:
    # Insert the key, with the specified value.
# values(): Returns a list of all the values in the dictionary.

# clear(): Removes all the elements from the dictionary
