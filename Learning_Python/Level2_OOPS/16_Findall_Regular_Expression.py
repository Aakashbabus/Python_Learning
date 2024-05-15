# Regular Expression or reg|ex

# The findall() function in Python's re module is used to find all non-overlapping matches of a pattern in a string.
# It searches the entire input string and returns a list of all occurrences of the pattern, or an empty list if no
# matches are found.

import re

keyword = "apple"

# check 1
if re.findall(keyword,"apple is on the tray  "):
    print(re.findall(keyword, "apple is on the tray  "))
    print("Match found")
else:
    print("No match found")

# check 2
if re.findall(keyword,"apples is on the tray  "):
    print(re.findall(keyword, "apples is on the tray  "))
    print("Match found")
else:
    print("No match found")

# check 3
if re.findall(keyword,"app is on the tray  "):
    print(re.findall(keyword,"app is on the tray  "))
    print("Match found")
else:
    print("No match found")

# check 4
if re.findall(keyword," on the tray is an apple"):
    print(re.findall(keyword," on the tray is an apple"))
    print("Match found")
else:
    print("No match found")