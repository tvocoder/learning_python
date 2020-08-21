# Strings are Arrays
# Arrays of bytes representing unicode characters.
# A single character is a string of length 1.

str = "My name is Tuan"
age = 31

# Check String
chk_str = "Tuan"
# not in -- checks if phrase is not in string
is_true = chk_str in str
if(is_true):
    print("Phrase is in string")
else:
    print("Phrase is not in string")

# Concatenation cannot combine strings and numbers
# format() is used to combine both strings numbers
txt = str + "and I am {}"
new_str = txt.format(age)
print(new_str)

# format() method takes unlimited number of arguments,
# and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed
# in the correct placeholders:
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Slicing
str_slice = str[3:8]
print(str_slice)

# Length
str_length = len(str)
print(str_length)

# String Methods:

# strip(): method removes any whitespace from beginning to end
# -- returns a trimmed version of the string

# lower(): returns lower case string
# upper(): returns uppercase string
# swapcase(): swaps cases
# -- lower case becomes upper case
# -- upper case becomes lower case

# translate(): returns a translated string

# zfill(): fills the string with a specified number of 0 values at the beginning

# replace(): replaces a string with another string

# capitalize(): converts the first character to upper case
# casefold(): converts string into lower case
# center(): returns a centered string
# count(): returns the number of times a specified value occurs in a string
# encode(): returns an encoded version of the string

# startswith(): returns True if the string starts with the specified value
# endswith(): returns True if the string ends with the specified value

# expandtabs(): sets the tab size of the string

# find(): searches the string for a specified value and returns
# -- the position where it was found

# format(): formats specified values in a string
# format_map(): formats a specified values in a string

# index(): searches the string for a specified value
# -- returns the position of where it was found

# isalnum(): returns True if all characters in the string are alphanumeric
# isdecimal(): returns True if all characters in the string are decimals
# isdigit(): returns True if all characters in the string are digits
# islower(): returns True if all characters in the string are lower case
# isnumeric: returns True if all characters in the string are numeric
# isprintable(): returns True if all characters in the string are printable
# isspace(): returns True if all characters in the string are whitespaces
# istitle(): returns True if the string follows the rules of a title
# isupper(): returns True if all characters in the string are upper case

# isidentifier(): returns True if the string is an identifier

# join(): joins the elements of an iterable to the end of the string

# ljust(): returns a left justified version of the string
# rjust(): returns a right justified version of the string

# lstrip(): returns a left version of the string
# rstrip(): returns a right version of the string

# split(): splits the string at the specified separator
# -- returns a list
# rsplit(): splits the string at the specified separator
# -- returns a list
# splitlines(): splits the string at line breaks
# -- returns a list

# maketrans(): returns a translation table to be used in translations

# partition(): returns a tuple where the string is parted into three parts
# rpartition(): returns a tuple where the string is parted into three parts

# replace(): returns a string where a specified value is replaced with a specified value

# rfind(): searches the string for a specified value
# -- returns the last position of where it was found
# rindex(): searches the string for a specified value
# -- returns last position of where it was found


