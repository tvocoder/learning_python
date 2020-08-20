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
