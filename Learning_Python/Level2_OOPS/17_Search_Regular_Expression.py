# Regular Expression or reg|ex

# In Python, the re.search() function is part of the re module, which provides support for regular expressions (regex).
# re.search() is used to search for a pattern anywhere in a string. If the pattern is found within the string,
# re.search() returns a match object; otherwise, it returns None.

import re

keyword = "apple"

# check 1
if re.search(keyword, "apple is on the tray  "):
    print("Match found")
else:
    print("No match found")

# check 2
if re.findall(keyword, "apples is on the tray  "):
    print("Match found")
else:
    print("No match found")

# check 3
if re.search(keyword, "app is on the tray  "):
    print("Match found")
else:
    print("No match found")

# check 4
if re.findall(keyword, "on the tray is apple  "):
    print("Match found")
else:
    print("No match found")
