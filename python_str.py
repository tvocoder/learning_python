# str: The items of a string are characters.
# Characters represent (at least) 8 bit bytes.
# The built-in functions chr() and ord() convert between characters and nonnegative integers representing byte values.
# Bytes with the values 0-127 usually represent the corresponding ASCII values, but interpretation of values is
# up to the program.
# String data type is also used to represent arrays of bytes, e.g., to hold data read from a file.
# Strings are immutable sequences.

print("---= CONSTRUCTOR =---")

print("-- str() --")
# Description: Returns a string containing a printable representation of an object.
# Syntax: str(object)
# -- object: Optional. Any Object. If omitted an emptry string is returned.
# Return Value: str
# Time Complexity:
# Remarks: Returns a string containing a printable representation of an object.
# -- For strings, this returns the string itself.
# -- The difference with repr(object) is that str(object) does not always attempt to return a string that is acceptable
# -- to eval(); its goal is to return a printable string. See also unicode().


# Example:

# string -- dict
print(str({'a': 1, 'b': 2}))

# string -- list
print(str([1, 2, 3]))

# string -- set
print(str((1, 2)))
print("*************************")

print(str('foobar'))
print(repr('foobar'))

bool = bool(str('foobar') == repr('foobar'))
print(bool)

print("-- x'string'(string designators) --")
# Description: Returns a modified string.
# Syntax: [designator]string
# -- r|R : Raw string. Uses different rules for interpreting backslash escape sequences.
# -- u|U : Unicode string.
# -- b|B : Alias for bytes type; it indicates the literal should become a bytes literal in Python 3
# -- Ur|UR|Ur|uR : Raw Unicode.
# -- br|Br|bR|BR : Raw Bytes
# Return Value:
# Time Complexity:
# Remarks:

# Example:
s = u'ABCD'
print(s)

s = b'ABCD'
print(s)
print("*************************")

print("-- Literal Syntax --")
# Description: String literals can be enclosed in matching single quotes(') or double quotes(").
# Syntax:
# Return Value:
# Time Complexity:
# Remarks: Unescaped quotes of same type as the one that was used for creating the string can't be used inside of it

# Example(s):
# Multiple adjacent string literals(delimited by whitespace), possibly using different quoting conventions,
# -- are allowed, and their meaning is the same as their concatenation.
# -- Thus, "hello"'world' is equivalent to "helloworld".
# -- The '+' operator must be used to concatenate string expressions at run time.
s = 'AB' "CD"
print(s)

# The backslash(\) character is used to escape characters that otherwise have a special meaning, such as
# -- newline, backslash itself, or the quote character.
print("AA\nBB")
print("*************************")

print("---= METHODS =---")

print("--= Searching =--")
print("-- find() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- rfind() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- index() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- rindex() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")

print("--= Replacing =--")
print("-- replace() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- translate() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")

print("--= Leading and Trailing Characters --=")
print("-- lstrip() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- rstrip() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- strip() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")

print("--= Splitting and Joining =--")
print("-- split() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- rsplit() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- partition() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- rpartition() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- splitlines() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- join() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")

print("--= Changing Case =--")
print("-- upper() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- lower() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- capitalize() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- title() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- swapcase() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")

print("--= Information =--")
print("-- count() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- startswith() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- endswith() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- isalnum() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- isalpha() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- isdigit() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- islower() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- isspace() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- istitle() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- isupper() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")

print("--= Formatting =--")
print("-- ljust() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- rjust() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- center() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- zfill() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- expandtabs() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- `format`_ --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")

print("--= Encodings =--")
print("-- decode() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- encode() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")

print("---= FUNCTIONS =---")

print("-- len() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- min() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- max() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- cmp() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- sorted() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- reversed() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- all() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- any() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- enumerate() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- zip() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- chr() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- ord() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- unichr() --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print(" -- `format`_ --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")

print("--= Operators =--")
print("-- `%(string formating)`_ --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- [](index operator) --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- [::](slicing) --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- +(concatenation) --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")
print("-- *(multiple concatenation) --")
# Description:
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")

print("--= Misc =--")
print("-- Escape Characters --")
print("-- ASCII Table (0-127) --")