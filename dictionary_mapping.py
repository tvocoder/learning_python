# geeksforgeeks.org

# Function to convert number into string
# Switcher is dictionary data type here

def numbers_to_strings(argument):

    switcher = {
        0: "Zero",
        1: "One",
        2: "Two",
    }
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "nothing")

# Driver program
if __name__ == "__main__":
    argument = 0
    print(numbers_to_strings(1))

# key value pairs
d = dict()
print(d)
d['xyz'] = 1
d['abc'] = 2
d['lmn'] = 3
print(d)

# print keys
print(d.keys())
print(d.values())
# del d['abc']
print(d.values())
# exists
print('xyz' in d)

# dictionary 2
# len function
print(d)
# of key value pairs
print(len(d))
# convert into string
str1 = str(d)
print(str1)
# dictionary to string
# print first five 5 values
print(str1[0:5:1])
# items function
# return list with all dictionary keys with their respective values
print(d.items())
# key values pairs are printed in no particular order

# copy of one dictionary into another
d2 = {}
d2 = d.copy()
print(d2)
# clear dictionary
d.clear()
print(d)

# dictionary pt3
# update
d1 = {'Name': 'Tuan', 'Age': 31}
d2 = {'Roll_Number': 2015155}
d1.update(d2)
print(d1)

# get(key, def_value) function
name = {"Name": "Tuan"}

# dictionary.get(keyname, value)
# keyname -- Required -- The keyname of the item you want to return the value from
# value -- Optional -- A value to return if the specified key does not exist.
# returns value if keyname is present in object
print(name.get("Name", "Not Present"))
print(name.get("Roll_Number", "Not Present"))
print(name)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# if --value --"model" is not found --return --value
x = car.get("model", 15000)
print(x)

