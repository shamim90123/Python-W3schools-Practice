name = "John"
age = 50
print(name)
print(age)

stringInt = 3
stringInt = "Three"
print(stringInt)

# Casting:-- If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

# Get the Type:-- You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

# Single or Double Quotes:-- String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'

# Case-Sensitive:-- Variable names are case-sensitive.
a = 4
A = "Sally"
print(a)
# A will not overwrite a

# Variable Names:-- A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)
