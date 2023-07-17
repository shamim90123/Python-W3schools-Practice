print("Hello, World!")


# if 5 > 2:
#     print("Five is greater than two!")

# // this will not work in python:---  You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
# if 5 > 2:
#  print("Five is greater than two!")
#         print("Five is greater than two!")

# Python Variables:-- Python has no command for declaring a variable.
# x = 5
# y = "Hello, World!"

# Python comments:-- Python has commenting capability for the purpose of in-code documentation.
# This is a single line comment.
"""
This is a
multiline docstring.
"""

# Unpack a Collection
# fruits = ['ginger', 'garlic', 'onion', 'turmeric', 'chili']
# ginger, garlic, onion, turmeric, chili = fruits
# print(ginger)
# print(garlic)
# print(onion)
# print(turmeric)
# print(chili)

# Global Variables
# spice = "ginger"

# def myfunc():
#     global spice
#     spice = "garlic"
#     print("Spice is " + spice)

# myfunc()

# print("Spice is " + spice)

# random
import random

print(random.randrange(1, 100))

#format()

# price = 49
# txt = "Turmeric price is {} takas"
# print(txt.format(price))

# Check if Item Exists
# spices = ["ginger", "garlic", "onion", "turmeric", "chili"]

# if "turmeric" in spices:
#     print("Yes, 'turmeric' is in the spices list")

# Loop Through a List
# for x in spices:
#     print(x)