# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:29:28 2024

@author: chien
"""

line01 = "******************************" # header / footer
line02 = "*                            *" # re-use

from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Example usage:
birthdate = date(1972, 4, 23)
line03 = "* Age: " + str(calculate_age(birthdate)) + " years oldclea          *"  # Output: 52

# agecalc = calculate_age(birthdate)

print('')

# Calculate the age

calcage = calculate_age(birthdate)
meaning = calcage

# if-else-Statement
if meaning > 10: 
    line06 = "* " + ('Right On') + "                   *"
else: 
    line07 = "* " + ('Not Today') + "                  *"

print('')

# Ternary Operator
line04 = "* " + ('Right On!' if meaning > 10 else 'Not Today') + "                  *"
line05 = "* " + ('You\'re 52 years old, today' if meaning >= calcage else 'Your age is not enough today') + " *"


# Output 
print(line01)
print(line02)
print(line03)
print(line04)
print(line05)
print(line06)
print(line02)
print(line01)
