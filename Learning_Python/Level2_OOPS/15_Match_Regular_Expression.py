# Regular Expression or reg|ex

# In Python, the re.match() function is part of the re module, which provides support for regular expressions (regex).
# re.match() is used to search for a pattern at the beginning of a string. If the pattern is found at the start of the
# string, re.match() returns a match object; otherwise, it returns None.

import re

keyword = "apple"

# check 1
if re.match(keyword,"apple is on the tray  "):
    print("Match found")
else:
    print("No match found")

# check 2
if re.match(keyword,"apples is on the tray  "):
    print("Match found")
else:
    print("No match found")

# check 3
if re.match(keyword,"app is on the tray  "):
    print("Match found")
else:
    print("No match found")

# check 4
if re.match(keyword," on the tray is an apple"):
    print("Match found")
else:
    print("No match found")