# w3school & python-reference.readthedocs.io
# Python Operators
# Operators are used to perform operations on variables and values.

# -- Arithmetic Operators
# --- Used with numeric values to perform common mathematical operations
val1 = 5
val2 = 25
txt1 = "Hello"
txt2 = "World"
is_true = True

print("Arithmetic Operators")
# addition
# -- returns the sum of two expressions
result = val1 + val2
print(result)
print(".............")

# subtraction
# -- returns the difference of two expressions
result = val1 - val2
print(result)
print(".............")

# multiplication
# -- returns the product of two expressions
result = val1 * val2
print(result)
print(".............")

# division
# -- returns the quotient of two expressions
result = val2 / val1
print(result)
print(".............")

# modulus
# -- returns the decimal part (remainder) of the quotient
result = val2 % val1
print(result)
print(".............")

# exponentiation
# -- returns the value of a numeric expression raised to a specific power
result = val2 ** val1
print(result)
print(".............")

# floor division
# -- returns the integral part of the quotient
result = val2 // val1
print(result)
print(".............")

print("..........................\n")

# -- Assignment Operators
print("Assignment Operators")
val1 = 5
val2 = 25
txt1 = "Hello"
txt2 = "World"

# = (simple assignment)
# -- Assigns a value to a variable(s)
new_val = val1 + val2
new_txt = txt1 + " " + txt2

print(new_val)
print(new_txt)
print(".............")

# += (increment assignment)
# -- Adds a value and the variable and assigns
# --- result to that variable
new_val += val1
print(new_val)
print(".............")

# -= (decrement assignment)
# -- Subtracts a value from the variable and assigns
# --- result to that variable
new_val = val2
new_val -= val1
print(new_val)
print(".............")

# *= (multiplication assignment)
# -- Multiplies the variable by a value and assigns
# --- result to that variable
new_val = val2
new_val *= val1
print(new_val)
print(".............")

# /= (division assignment)
# -- Divides the variable by a value and assigns
# --- result to that variable
new_val = val2
new_val /= val1
print(new_val)
print(".............")

# **= (power assignment)
# -- Raises the variable to a specified power and assigns
# --- result to the variable
new_val = val2
new_val **= val1
print(new_val)
print(".............")

# %= (modulus assignment)
# -- Computes the modulus of the variable and a value and assigns
# --- result to that variable
new_val = val2
new_val %= val1
print(new_val)
print(".............")

# //= (floor division assignment)
# -- Floor divides the variable by a value and assigns
# --- result to that variable
new_val = val2
new_val //= val1
print(new_val)
print(".............")

print("..........................\n")

# Relational Operators
print("Relational Operators")
val1 = 5
val2 = 25
txt1 = "Hello"
txt2 = "World"
is_true = True

# == (equal)
# -- Returns a Boolean string whether two expressions are equal.
is_true = val1 < val2
print(is_true)
print(".............")

# != (not equal)
# -- Returns a Boolean stating whether two expressions are not equal.
is_true = val1 != val2
print(is_true)
print(".............")

# > (greater than)
# -- Returns a Boolean stating whether one expression is greater than the other.
is_true = val2 > val1
print(is_true)
print(".............")

# >= (greater than or equal)
# -- Returns a Boolean stating whether one expression is greater than the other.
is_true = val2 > val1
print(is_true)
print(".............")

# < (less than)
# -- Returns a Boolean stating whether one expression is less than the other.
is_true = val1 < val2
print(is_true)
print(".............")

# <= (less than or equal)
# -- Returns a Boolean stating whether one expression is less than or equal to the other.
is_true =  val1 <= val2
print(is_true)
print(".............")

print("..........................\n")

# Boolean Operators
print("Boolean Operators")
val1 = 5
val2 = 25
txt1 = "Hello"
txt2 = "World"
is_true = True

# and
# -- Returns the first operand that evaluates to
# ---False or the last of all are True.
is_true = txt1.isprintable() and txt2.isprintable()
print(is_true)
print(".............")

# or
# -- Returns the first operand that evaluates to
# --- True or the last one if all are False
is_true = txt1.isalpha() or txt2.isalpha()
print(is_true)
print(".............")

# not
# -- Returns a boolean that is the
# --- reverse of the logical state of an expression.
is_true = not txt1.isprintable()
print(is_true)
print(".............")

print("..........................\n")

# Conditional Operator
print("Conditional Operator")
val1 = 5
val2 = 25
txt1 = "Hello"
txt2 = "World"
is_true = True

# if else -- A if expression else B
# -- A (the value for the entire conditional expression if True)
# -- expression (condition that evaluates to a Boolean)
# -- B (the value for the entire conditional expression if False)
# -- Returns either value depending on
# --- result of a Boolean expression
print(".............")

print("..........................\n")

# Identity
print("Identity")
val1 = 5
val2 = 25
txt1 = "Hello"
txt2 = "World"
is_true = True

# is -- A is [not] B
# # A: any object
# # B: any object
# -- Returns a Boolean stating whether two objects are the same.
is_true = txt1 is txt2
print(is_true)
print(".............")

print("..........................\n")

# Membership
print("Membership")
val1 = 5
val2 = 25
txt1 = "Hello"
txt2 = "World"
is_true = True

# in -- A [not] in B
# -- A: any valid object
# -- B: any valid object
# -- Time Complexity: O(1) for dict O(1) to O(n) for sets O(n) for sequences
# --- -str -list -tuple
# -- Remarks: When used with dictionaries checks the keys instead of values.
# -- Returns a Boolean string whether the object is in the container.
is_true = txt1 not in txt2
print(is_true)
print(".............")

print("..........................\n")

# Deletion
print("Deletion")
val1 = 5
val2 = 25
txt1 = "Hello"
txt2 = "World"
is_true = True

# del
# -- Removes object
new_txt = str(txt1)
print(new_txt)
del new_txt
print("..........................\n")

# Callables Operators
print("Callable Operators")
val1 = 5
val2 = 25
txt1 = "Hello"
txt2 = "World"
is_true = True

# * (tuple packing)
# -- Syntax: def function(*tuple):
# -- tuple: object used for storing passed in arguments.
# -- Remarks: the tuple name *args is used by convention.
# -- Packs the consecutive function positional arguments into a tuple.
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3))
print(".............")

# ** (dictionary packing)
# -- Syntax: def function(**dict):
# -- dict: object used for storing the passed in arguments.
# -- Remarks: the dict name **kwargs is used by convention.
# -- Packs the consecutive function keyword arguments into a dictionary.
def example(**kwargs):
    return kwargs.keys()

print(example(a = 10, b = 20, c = [0,0,0]))
print(".............")

# * (tuple unpacking)
# -- Syntax: function(*iterable)
# -- iterable: iterable object containing the positional arguments.
# -- Unpacks the contents of a tuple into the function call.
def add(a,b):
    return a + b
t = (2,3)

print(add(*t))
print(t)
print(".............")

# ** (dictionary unpacking)
# Syntax: function(**dict)
# -- dict: dictionary containing pairs of keyword arguments and their values.
# -- Unpacks the contents of a dictionary into the function call.
def add(a = 0, b = 0):
    return a + b

d = {'a': 2, 'b': 3}
print(add(**d))
print(d)
print(".............")

# @ (decorator)
# -- Returns a callable wrapped by another callable.
print(".............")

# lambda
# -- Returns an anonymous function.
print(".............")

# () (call operator)
# -- Calls a callable object with specified arguments.
print(".............")

print("..........................\n")

# Bitwise Operators
print("Bitwise Operators")
val1 = 5
val2 = 25
txt1 = "Hello"
txt2 = "World"
is_true = True

# & (bitwise AND)
# -- Returns the result of bitwise AND of two integers.
print(".............")

# | (bitwise OR)
# -- Returns the result of bitwise OR of two integers.
print(".............")

# ^ (bitwsie XOR)
# -- Returns the result of bitwsie XOR of two integers.
print(".............")

# << (left shift)
# -- Shifts the bits of the first operand left
# --- by the specified number of bits.
print(".............")

# >> (right shift)
# -- Shifts the bits of the first operand right
# --- by the specified number of bits.
print(".............")

# ~ (bitwise complement)
# -- Sets the 1 bits to 0 and 1 to 0 and then adds 1
print(".............")

print("..........................\n")

# Bitwise Assignment Operators
print("Bitwise Assignment Operators")
val1 = 5
val2 = 25
txt1 = "Hello"
txt2 = "World"
is_true = True

# &= (bitwise AND assignment)
# -- Performs bitwise AND and assigns value to the left operand.
print(".............")

# |= (bitwise OR assignment)
# -- Performs bitwise OR and assigns value to the left operand.
print(".............")

# ^= (bitwise XOR assignment)
# -- Performs bitwise XOR and assigns value to the left operand.
print(".............")

# <<= (bitwise right shift assignment)
# -- Performs bitwise left shift and assigns value to the left operand.
print(".............")

# >>= (bitwise left shift assignment)
# -- Performs bitwise right shift and assigns value to the left operand.
print(".............")

print("..........................\n")

# Misc
print("Misc")
val1 = 5
val2 = 25
txt1 = "Hello"
txt2 = "World"
is_true = True

# ; (statement separator)
# -- Separates two statements.
print(".............")

# (line continuation)
# -- Breaks the line of code allowing for the next line continuation.
print(".............")

# .(attribute access)
# -- Gives access to an object's attribute.
print(".............")

print("..........................\n")

# String and Sequence Operators
print("String and Sequence Operators")
val1 = 5
val2 = 25
txt1 = "Hello"
txt2 = "World"
is_true = True

# +(concatenation)
# -- Returns a concatenation of two sequences
print(".............")

# *(multiple concatenation)
# -- Returns a sequence of self-concatenated specified amount of times.
print(".............")

# %(string formatting operator)
# -- Formats the string according to the specified format.
print(".............")

print("..........................\n")

# Sequence Assignment Operators
print("Sequence Assignment Operators")
val1 = 5
val2 = 25
txt1 = "Hello"
txt2 = "World"
is_true = True

# +=(concatenation assignment)
# -- Concatenates the sequence with the right operand and
# --- assigns the result to that sequence
print(".............")

# *=(multiple concatenation assignment)
# -- Multiple concatenates the sequence and
# --- assigns the result to that sequence.
print(".............")

print("..........................\n")
