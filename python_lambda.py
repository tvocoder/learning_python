print("---= Lambda Function =---")
# Description: Returns an anonymous function
# Syntax: lambda variable, ...: expression
# -- variable: Optional. One more variables used in the right part of the expression.
# -- expression: Required. Return value of the function.
# Remarks: lambda expression is a short hand way of defining a function that is not bound to a specified name during,
# -- its creation.

# Example:
func = lambda x: x + 1
print(func(10))

# Lambda function with sorted function
# -- garbage collected after it has been used.
# (there is no reference to keep it alive)

print(sorted(['A', 'b', 'C'], key= lambda x: x.lower()))
