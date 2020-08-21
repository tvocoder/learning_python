# Python built-in data types
# Text type: str
# Num type: int, float, complex
# Sequence type: list, tuple, range
# Mapping type: dict
# Set types: set, frozenset
# Boolean type: bool
# Binary types: bytes, bytearray, memoryview

# Getting the Data Type -- type() function
# string
val = 'Datatype?'
print(type(val))

set_val = str("Hello")
print(set_val)
print(".............")

# int
val = 25
print(type(val))

set_val = int(25)
print(set_val)
print(".............")

# float
val = 25.5
print(type(val))

set_val = float(25.5)
print(set_val)
print(".............")

# complex
val = 1j
print(type(val))

set_val = complex(1j)
print(set_val)
print(".............")

# list
val = ["one","two","three","four"]
print(type(val))

set_val = list(("one", "two", "three"))
print(set_val)
print(".............")


# tuple
val = ("one", "two", "three", "four")
print(type(val))

set_val = tuple(("one", "two", "three"))
print(set_val)
print(".............")

# range
val = range(10)
print(type(val))

set_val = range(10)
print(set_val)
print(".............")

# set
val = {"one", "two", "three"}
print(type(val))

set_val = set(("one","two", "three"))
print(set_val)
print(".............")

# frozenset
val = frozenset({"one", "two", "three"})
print(type(val))

set_val = frozenset(("one","two", "three"))
print(set_val)
print(".............")

# bool
val = True
print(type(val))

set_val = bool(10)
print(set_val)
print(".............")

# bytes
val = b"Hello"
print(type(val))

set_val = bytes(5)
print(set_val)
print(".............")

# bytearray
val = bytearray(5)
print(type(val))

set_val = bytearray(5)
print(set_val)
print(".............")

# memoryview
val = memoryview(bytes(5))
print(type(val))

set_val = memoryview(bytes(5))
print(set_val)
print(".............")