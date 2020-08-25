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
# Description: Returns the index of the first occurrence of the string searched for.
# Syntax: str.find(sub[,start[,end]])
# -- sub: Required. The string searched for.
# -- start: Optional. Search start position.
# -- end: Optional. Search end position.
# Return Value: int
# Time Complexity:
# Remarks: Returns -1 if sub is not found.
# -- The find() method should be used only if you need to know the position of sub.
# -- To check if sub is a substring or not, use the in operator.

# Example:
s = "Hello World"
search = "hello"

found = search.upper() in s.upper()
print(found)

found_idx = s.find("World")
print(found_idx)
print("*************************")

print("-- rfind() --")
# Description: Returns the index of the last occurence of the string searched for.
# Syntax: str.rfind(sub[,start[,end]])
# -- sub: Required. The string searched for.
# -- start: Optional. Search start position.
# -- end: Optional. Search end position.
# Return Value: int
# Time Complexity:
# Remarks: Returns -1 if sub(string) is not found
# -- The rfind() method should be used only if you need to know the position of sub.
# -- To check if sub is a substring or not, use the in operator:

# Example:
found = "ABAB".rfind("B")
print(found)

found_1 = "ABAB".rfind("B", 0, 2)
print(found)

found_2 = "ABAB".rfind("B", 2)
print(found)
print("*************************")

print("-- index() --")
# Description: Returns the index of the last occurrence of the string searched for(raises ValueError if not found).
# Syntax: str.index(sub[,start[,end]])
# -- sub: Required. The string searched for.
# -- start: Optional. Search start position.
# -- end: Optional. Search end position.
# Return Value: int
# Time Complexity:
# Remarks: Raises ValueError if not found

# Example:
idx_loc = "ABAB".index("B")
print(idx_loc)

idx_loc_1 = "ABAB".index("B", 2, 4)
print(idx_loc_1)

idx_loc_2 = "ABAB".index("B", 2)
print(idx_loc_2)
print("*************************")

print("-- rindex() --")
# Description: Returns the index of the first occurrence of the string searched for.
# Syntax: str.rindex(sub[,start[,end]])
# -- sub: Required. The string searched for.
# -- start: Optional. Search start position.
# -- end: Optional. Search end position.
# Return Value: int
# Time Complexity:
# Remarks: Raises ValueError if not found.

# Example:
idx_loc = "ABAB".rindex("B")
print(idx_loc)

idx_loc = "ABAB".rindex("B", 2, 4)
print(idx_loc)

idx_loc = "ABAB".rindex("B", 2)
print(idx_loc)
print("*************************")

print("--= Replacing =--")
print("-- replace() --")
# Description: Returns a copy of the string with a specified substring replaced specified number of times.
# Syntax: str.replace(old, new[,count])
# -- old: Required. String to be replaced.
# -- new: Optional. String to replace the old one.
# -- count: Optional. Number of old occurrences to replace.
# Return Value: str
# Time Complexity:
# Remarks:

# Example:
print("ABCAB".replace('AB', 'ab'))

s = "ABCAB"
t = "AB"
r = "ab"
print(s.replace(t, r, 1))
print("*************************")

print("-- translate() --")
# Description: Returns a copy of the string with characters mapped through the given translation table or deleted.
# Syntax: str.translate(table[,deletechars])
# -- table: Required. Must be a string of length 256.
# -- deletechars: Optional. Characters to be deleted from the string.
# Return Value: str
# Time Complexity:
# Remarks: You can use the maketrans() helper function in the string module to create a translation table.
# -- For string Objects, set the table argument to None for translations that only delete characters.

# Example(s):
# Delete all the vowels from the string
# print("ABCDE".translate("AEIOU"))
print("*************************")

print("--= Leading and Trailing Characters --=")
print("-- lstrip() --")
# Description: Returns a copy of the string with leading characters removed.
# Syntax: str.lstrip([chars])
# -- chars: Optional. String specifying the set of characters to be removed. If omitted or None, the chars argument
# defaults to remove whitespace. The chars argument is not a prefix; rather, all combinations of its values are strip.
# Return Value: str
# Time Complexity:
# Remarks:

# Example:
print('    spacious   '.lstrip())

s = "AABAA"
s_strip = s.lstrip("AB")
print(s_strip)
print("*************************")

print("-- rstrip() --")
# Description: Returns a copy of the string with trailing characters removed.
# Syntax: str.rstrip([chars])
# -- chars: Optional. String specifying the set of characters to be removed. If omitted or None, the chars argument
# defaults to removing whitespace. The chars argument is not a prefix; rather, all combinations of its values are strip.
# Return Value: str
# Time Complexity:
# Remarks:

# Example:
print('    spacious    '.rstrip())

s = "AABAA"
print(s.rstrip("AA"))
print("*************************")

print("-- strip() --")
# Description: Returns a copy of the string with the leading and trailing characters removed.
# Syntax: str.strip([chars])
# -- chars: Optional. String specifying the set of characters to be removed. If omitted or None, the chars argument
# defaults to removing whitespace. The chars arg is not a prefix; rather, all combinations of its values are stripped.
# Return Value: str
# Time Complexity:
# Remarks:

# Example:
strip = '    spacious    '.strip()
print(strip)

print("ABBA".strip("AB"))
print("*************************")

web_addr = "www.example.com"
web_addr_strip = web_addr.strip('cmowz')
print(web_addr_strip)

print("--= Splitting and Joining =--")
print("-- split() --")
# Description: Returns a list of the words in the string, separated by the delimiter string.
# Syntax: str.split([sep[,maxsplit]])
# -- sep: Optional. Character dividing the string into split groups; default is space.
# -- maxsplit: Optional. Number of splits to do; default is -1 which splits all the items.
# Return Value: list
# Time Complexity:
# Remarks: If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings.

# Example:
s = '1,,2'
s_list = s.split(',')

s = "1 2 3 4 5"
s_list = s.split()
print(s_list)
print("*************************")

print("-- rsplit() --")
# Description: Returns a list of the words in the string, separated by the delimiter string (starting from right).
# Syntax: str.rsplit([sep[,maxsplit]])
# -- sep: Optional. Character dividing the string into split groups; default is space.
# -- maxsplit: Optional. Number of splits to do; default is -1 which splits all the items.
# Return Value: list
# Time Complexity:
# Remarks:

# Example:
print(' a b c'.rsplit())

print("----a---b--c-'".rsplit('-'))
print("*************************")

print("-- partition() --")
# Description: Returns a tuple containing the left part of the string split by the specified separator,
# the separator itself and the right part of the string.
# Syntax: str.partition(sep)
# -- sep: Required. Separator for the returned tuple. If the separator is not found, partition returns a 3-tuple
# containing the string itself, followed by two empty strings.
# Return Value: tuple
# Time Complexity:
# Remarks:

# Example:
print("AB-CD-EF".partition('-'))

# This example breaks image file-path into its components
img = "image.png"
t = "image.png".partition('.')
print(t)
print("*************************")

print("-- rpartition() --")
# Description: Returns a tuple containing the left part of the string split by the specified separator,
# the separator itself and the right part of the string (starting from the right).
# Syntax: str.rpartition(sep)
# -- sep: Required. Separator for the returned tuple. If the separator is not found, partition returns a 3-tuple,
# containing two empty strings, followed by the string itself.
# Return Value: tuple
# Time Complexity:
# Remarks:

# Example:
t = "AB-CD-EF".rpartition("-")
print(t)

t = "image.png".rpartition(".")
print(t)
print("*************************")

print("-- splitlines() --")
# Description: Returns a list of the lines in the string, breaking at line boundaries.
# Syntax: str.splitlines([keepends])
# -- keepends: Optional. When set to True line breaks are included in the resulting list.
# Return Value: list
# Time Complexity:
# Remarks: This method uses the universal newlines approach to splitting lines.
# -- Unlike split() when a delimiter string sep is given, this method returns an empty list for the empty string,
# and a terminal line break does not result in an extra line.

# Example:
s = "AB\nCD\n"
print(s)
l = s.splitlines()
print(l)
print("*************************")

print("-- join() --")
# Description: Returns a string made from the elements of an iterable.
# Syntax: str.join(iterable)
# -- iterable: Required. The iterable used for creating the string.
# Return Value: str
# Time Complexity:
# Remarks: The separator between elements is the string providing this method.

# Example:
l = ['A', 'B', 'C', 'D', 'E', 'F']
s = ' '.join(l)
print(s)
print("*************************")

print("--= Changing Case =--")
print("-- upper() --")
# Description: Returns a copy of the string in UPPER CASE.
# Syntax: str.upper()
# Return Value:
# Time Complexity:
# Remarks: Note that s.upper().isupper() might be False if s contains uncased characters or if the Unicode category of
# -- the resulting character(s) is not "Lu" (Letter, uppercase), but e.g. "Lt" (Letter, titlecase)
# For 8-bit strings, this method is locale-dependent.

# Example:
s = 'abc'.upper()
is_true = s.isupper()

print(s)
print(is_true)
print("*************************")

print("-- lower() --")
# Description: Returns a copy of the string in lower case.
# Syntax: str.lower()
# Return Value: str
# Time Complexity:
# Remarks: For 8-bit strings, the method is locale-dependent.

# Example:
s = 'ABC'.lower()
is_true = s.islower()

print(s)
print(is_true)
print("*************************")

print("-- capitalize() --")
# Description: Returns a copy of the string in Capital case.
# Syntax: str.capitalize()
# Return Value: str
# Time Complexity:
# Remarks: For 8-bit strings, this method is locale-dependent.

# Example:
s = "hello"
print(s.capitalize())
print("*************************")

print("-- title() --")
# Description: Returns a copy of the string in Title Case.
# Syntax: str.title()
# Return Value: str
# Time Complexity:
# Remarks: The algorithm uses a simple language-independent defintion of a word as groups of consecutive letters.
# -- The definition works in many contexts but it means that apostrophes in contractions and possessives form word
# -- boundaries, which may not be the desired result.

# Example:
s = "they're bill's friends from the UK".title()
print(s)

# Workaround for apostrophes can be contructed using regular expressions
import re
def titlecase(str):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0)[0].upper() +
                  mo.group(0)[1:].lower(),str)
print(titlecase("they're bill's friends."))
print("*************************")

print("-- swapcase() --")
# Description: Returns a copy of the string with case swapped.
# Syntax: str.swapcase()
# Return Value: str
# Time Complexity:
# Remarks: For 8-bit strings, this method is locale-dependent.

# Example:
print('foo'.swapcase())

print('123'.swapcase())
print("*************************")

print("--= Information =--")
print("-- count() --")
# Description: Returns the number of non-overlapping occurences of a substring in the searched string.
# Syntax: str.count(sub[,start[,end]])
# -- sub: Required. The string searched for.
# -- start: Optional. Index form which to start counting. Default is 0 (start of the string)
# -- end: Optional. The end index for the search. End of the string is the default value.
# Return Value: int
# Time Complexity: Optional arguments start and end are interpreted as in slice notation.
# Remarks:

# Example:
s = "AAAAAAAAAAA"
print(s.count("A"))
print("*************************")

print("-- startswith() --")
# Description: Returns a Boolean stating whether a string starts with the specified prefix.
# Syntax: str.startswith(prefix[,start[,end]])
# -- prefix: Required. The substring looked for. prefix can also be a tuple of prefixes to look for.
# -- start: Optional. Specifies beginning position for the search.
# -- end: Optional. Specifies ending position for the search.
# Return Value: bool
# Time Complexity:
# Remarks:

# Example:
s = "log_A1.csv"
b = s.startswith("log")
print(b)
print("*************************")

print("-- endswith() --")
# Description: Returns a Boolean stating whether a string ends with the specified suffix.
# Syntax: str.startswith(suffix[,start[,end]])
# Return Value: bool
# Time Complexity:
# Remarks:

# Example:
s = "image.png"
s_2 = "image.gif"

b = s.endswith("png")
b_2 = s_2.endswith(("png", "gif"))

print(b)
print(b_2)
print("*************************")

print("-- isalnum() --")
# Description: Returns a Boolean stating whether the string contains only letters and digits.
# Syntax: str.isalnum()
# Return Value: bool
# Time Complexity:
# Remarks: For 8-bit strings, this method is locale-dependent. Returns False if string is empty.

# Example:
s = "abc12345"
b = s.isalnum()
print(b)

s = "!@#"
b = s.isalnum()
print(b)
print("*************************")

print("-- isalpha() --")
# Description: Returns a Boolean stating whether the string contains only letters.
# Syntax: str.isalpha()
# Return Value: bool
# Time Complexity:
# Remarks: For 8-bit strings, this method is locale-dependent. Returns False if string is empty.

# Example:
s = "abcdef"
print(s.isalpha())

s = "12345"
print(s.isalpha())
print("*************************")

print("-- isdigit() --")
# Description: Returns a Boolean string whether the string contains only digits.
# Syntax: str.isdigit()
# Return Value: bool
# Time Complexity:
# Remarks: For 8-bit strings, this method is locale-dependent. Returns False if string is empty.

# Example:
s = "12345"
print(s.isdigit())

s = "abcdef"
print(s.isdigit())
print("*************************")

print("-- islower() --")
# Description: Returns a Boolean stating whether the string is in lower case.
# Syntax: str.islower()
# Return Value: bool
# Time Complexity:
# Remarks: For 8-bit strings, this method is locale-dependent. Returns False if string is empty.

# Example:
s = "abcdef"
print(s.islower())

s = "12345"
print(s.islower())
print("*************************")

print("-- isspace() --")
# Description: Returns a Boolean stating whether the string contains only whitespace characters.
# Syntax: str.isspace()
# Return Value: bool
# Time Complexity:
# Remarks: For 8-bit strings, this method is locale-dependent. Returns False if string is empty.

# Example:
s = "     "
print(s.isspace())

s = "abcdef"
print(s.isspace())
print("*************************")

print("-- istitle() --")
# Description: Returns a Boolean stating whether the string is in Title case.
# Syntax: str.istitle()
# Return Value: bool
# Time Complexity:
# Remarks: For 8-bit strings, this method is locale-dependent. Returns False if string is empty.

# Example:
s = "Title"
print(s.istitle())

s = "title"
print(s.istitle())
print("*************************")

print("-- isupper() --")
# Description: Returns a Boolean stating whether the string is in UPPER CASE.
# Syntax: str.isupper()
# Return Value: bool
# Time Complexity:
# Remarks: For 8-bit strings, this method is locale-dependent. Returns False if string is empty.

# Example:
s = "ABCDEF"
print(s.isupper())

s = "abcdef"
print(s.isupper())
print("*************************")

print("--= Formatting =--")
print("-- ljust() --")
# Description: Returns the string left justified in a string of specified length.
# Syntax: str.ljust(width[,fillchar])
# -- width: Required. The width of the field containing the string.
# -- fillchar: Optional. Specifies the padding character (default is a space)
# Return Value: str
# Time Complexity:
# Remarks: The original string is returned if width is less than or equal to len(str)

# Example:
s = "abcdef"
s_new = s.ljust(10, "*")
print(s_new)
print("*************************")

print("-- rjust() --")
# Description: Returns the string right justified in a string of specified length.
# Syntax: str.rjust(width[,fillchar])
# -- width: Required. The width of the field containing the string.
# -- fillchar: Optional. Specifies the padding character (default is a space).
# Return Value: str
# Time Complexity:
# Remarks: The original string is returned if width is less than or equal to len(str)

# Example:
s = "abcdef"
s_new = s.rjust(10, "*")
print(s_new)
print("*************************")

print("-- center() --")
# Description: Returns the string centered in a string of specified length.
# Syntax: str.center(width[,fillchar])
# -- width: Required. The width of the field containing the string.
# -- fillchar: Optional. Specifies the padding character (default is a space).
# Return Value: str
# Time Complexity:
# Remarks:

# Example:
s = "abcdef"
s_new = s.center(10, "*")
print(s_new)
print("*************************")

print("-- zfill() --")
# Description: Returns the numeric string left filled with zeros in a string of specified length.
# Syntax: str.zfill(width)
# -- width: Required. Width of the padding field.
# Return Value: str
# Time Complexity:
# Remarks: A sign prefix handled correctly. The original string is returned if width is less than or equal to len(str).

# Example:
s = "281"
s_new = s.zfill(10)
print(s_new)
print("*************************")

print("-- expandtabs() --")
# Description: Returns a copy of the string where all tab characters were replaced by spaces.
# Syntax: str.expandtabs([tabsize])
# Return Value: str
# Time Complexity:
# Remarks: Tab positions occur every tabsize characters (default is 8, giving tab positions at columns 0, 8, 16, ...)
# -- To expand the string, the current column is set to zero and the string is examined character by character.
# -- If the character is a tab (t), one or more space characters are inserted in the result until the current column is
# -- equal to the next tab position. (The tab character itself is not copied). If the character is a newline (n) or
# -- return (r), it is copied and the current column is reset to zero. Any other character is copied unchanged and the
# --- current column is incremented by one regardless of how the character is represented when printed.

# Example:
s = "AA\tBB\n"
s_new = s.expandtabs()
print(s_new)
print("*************************")

print("-- `format`_ --")
# Description: Returns a formatted version of the string.
# Syntax:
# Return Value:
# Time Complexity:
# Remarks:

# Example:
print("*************************")

print("--= Encodings =--")
print("-- decode() --")
# Description: Decodes the string using the codec registered for encoding.
# Syntax: str.decode([encoding[,errors]])
# -- encoding: Optional. The desired encoding. Defaults to the default string encoding. Codecs module for a full list.
# -- errors: Optional. errors maybe given to a set a different error handling scheme.
# Typical Error Values:
# -- 'strict': Raises ValueError (or a subclass); this is the default.
# -- 'ignore': Ignore the character and continue with the next.
# -- 'replace': Replace with a suitable replacement character.
# Other possible values are any other name registered via codecs.register_error()
# Return Value: unicode
# Time Complexity:
# Remarks:

# Example:
print("*************************")

print("-- encode() --")
# Description: Returns an encoded version of the string.
# Syntax: str.encode([encoding[,errors]])
# -- encoding: Optional. The desired encoding. Defaults to the default string encoding. Codecs module for a full list.
# -- errors: Optional. errors maybe given to a set a different error handling scheme.
# Typical error values:
# -- 'strict': Raise ValueError (or a subclass): this is the default.
# -- 'ignore': Ignore the character and continue with the next.
# -- 'replace': Replace with a suitable replacement character.
# Return Value: str
# Time Complexity:
# Remarks:

# Example:
print('foo'.encode())
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
# Description: Returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument
# -- sequences or iterables
# Syntax: zip([iterable,...])
# -- iterable: Optional. An iterable object
# Return Value: list
# Time Complexity:
# Remarks: The returned list is truncated in length to the length of the shortest argument sequence.
# -- When there are multiple arguments which are all of the same length, zip() is similar to map() with an
# argument of None. With a single sequence argument, it returns a list of 1-tuples. With no args,
# empty list.
# -- The left-to-right evaluation order of the iterables is guaranteed. This makes possible an idiom for clustering
# a data series into n-length groups using zip(*[iter(s)]*n)

# Example:
l = zip('foo', 'bar')
print(*l)
print("*************************")

print("-- chr() --")
# Description: Returns a string of one character whose ASCII code is the specified number.
# Syntax: chr(number)
# -- number: Required. Any integer within the 0-255 range.
# Return Value: str
# Time Complexity:
# Remarks:

# Example:
print(chr(65))
print(chr(97))
print("*************************")

print("-- ord() --")
# Description: Returns an integer representing the code of the character
# Syntax: ord(character)
# -- character: Required. A character
# Return Value: int
# Time Complexity:
# Remarks: This function is the inverse of chr() for 8-bit strings and of unichr() for unicode objects.
# -- If a unicode argument is given and Python was built with UCS2 Unicode, then the character's code point must be
# in the range [0..65535] inclusive; otherwise the string length is two, and a TypeError will be raised.

# Example:
print(ord("A"))
print(ord("a"))
print("*************************")

print("-- unichr() --")
# Description: Returns a Unicode character specified by the code.
# Syntax: unichr(number)
# -- number: Required. An integer specifying the Unicode value of the character to be returned.
# Return Value: unicode
# Time Complexity:
# Remarks: This function is the inverse of ord() for Unicode strings.
# -- The valid range for the argument depends how Python was configured - it may be either UCS2[0..0xFFF] or
# UCS4[0..0x10FFFF]. ValueError is raised otherwise. For ASCII and 8-bit strings see chr().

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