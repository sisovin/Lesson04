# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 19:01:09 2024

@author: chien
"""

import math
from turtle import title

from flask import g

# String data type
print('====================String data type====================')
# literal assignment
print('====================literal assignment====================')

first = "Sisovin"
last = "CHIENG"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

print('=====================constructor function====================')
# constructor function
pizza = str("SeasoningShrimp")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

print('=================Concatenation====================')
# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

print('=================Casting a number to a string====================')
# Casting a number to a string
decade = str(1970)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

print('\n ==================Multi-line====================')
# Multi-line
multiline = '''
Hey, how are you?

I was just checking in.

                        All good?

'''
print(multiline)

print('\n====Escaping special characters====================')
# Escaping special characters
print('=====Original sentence that may contain backslashes')
# Original sentence that may contain backslashes
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'

# Replacing all backslashes with spaces
cleaned_sentence = sentence.replace('\\', ' ')

# Printing the cleaned sentence
print(cleaned_sentence)

print('\n=========String methods============================')
# String methods
print(first)
print(first.lower())
print(first.upper())
print(first.capitalize())
print(first.title())
print(first.swapcase())
print(first.center(20))
print(first.ljust(20))
print(first.rjust(20))
# print(first.zfill(20)) // Output: 000000000000Sisovin
print(first)

print('\n')
print(multiline.title())
print(multiline.replace('good', 'ok'))
print(multiline)

print('\n')
print(len(multiline))  #// Output: 80
multiline += "                  "
multiline = "                  " + multiline
print(len(multiline)) #// Output: 116

print('\n')
print(multiline.strip())
print(multiline.lstrip())
print(multiline.rstrip())

print("=====================================")
print("")

print("==================Build a Menu====================")
# Build a Menu
title = "menu".upper()
print(title.center(20, "=")) #// Output: ========MENU========
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
title = "end".upper()
print(title.center(20, "=")) #// Output: =========END========

print("===============String index values============")
# String index values
print(first[1]) #// Output: i from Sisovin (index 1)
print(first[-1]) # // Output: n from Sisovin (index -1)
print(first[1:-1]) # // Output: isovi from Sisovin (index 1 to -1)
print(first[1:]) # // Output: isovin from Sisovin (index 1 to end)

print("===============Some methods return boolean data====================")
# Some methods return boolean data
print(first.startswith("S")) # // Output: True
print(first.endswith("n")) # // Output: True
print(first.islower()) # // Output: False
print(first.isupper()) # // Output: False
print(first.isalpha()) # // Output: True

print("===============Boolean Data Type====================")
myvalue = True # // Output: True
x = bool(False) # // Output: False
print(type(x)) # // Output: <class 'bool'>
print(isinstance(myvalue, bool)) # // Output: True

print("===============Numeric Data Types====================")
# Numeric Data Types
print("===============Integers====================")
# Integers
price = 100
best_price = int(80)
print(type(price)) # // Output: <class 'int'>
print(isinstance(best_price, int)) # // Output: True
print(isinstance(price, int)) # // Output: True

print("===============Floats====================")
# Floats
gpa = 3.28
y = float(1.14)
print(type(gpa)) # // Output: <class 'float'>
print(isinstance(y, float)) # // Output: True
print(isinstance(gpa, float)) # // Output: True

print("===============Complex Numbers====================")
# Complex Numbers
comp_value = 3 + 4j
print(type(comp_value)) # // Output: <class 'complex'>
print(isinstance(comp_value, complex)) # // Output: True
print(comp_value.real) # // Output: 3.0
print(comp_value.imag) # // Output: 4.0

print("===============Build-in function for numbers====================")
# Build-in function for numbers
print(abs(gpa)) # // Output: 3.28
print(abs(-gpa)) # // Output: 3.28
print(abs(gpa * -1)) # // Output: 3.28

print(round(gpa)) # // Output: 3
print(round(gpa, 1)) # // Output: 3.3

print("===============Math module====================")
# Math module
print(math.pi) # // Output: 3.141592653589793
print(math.e) # // Output: 2.718281828459045
print(math.sqrt(64)) # // Output: 8.0
print(math.ceil(gpa)) # // Output: 4
print(math.floor(gpa)) # // Output: 3

print("===============Casting a string to a number====================")
# Casting a string to a number
zipcode = "90210"
zip_value = int(zipcode)
print(type(zip_value)) # // Output: <class 'int'>

print('\n')

# Error if you attempt to cast a string with letters to a number
# zip_value = int("90210A")
# Error if you attempt to cast incorrect data
# zip_value = int("Battambang")