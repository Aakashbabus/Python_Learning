#In Python, the re.sub() function is part of the re module, which provides support for regular expressions (regex).
# re.sub() is used to replace occurrences of a pattern in a string with a specified replacement string.

'''
re.sub(pattern, repl, string, count=0, flags=0)

pattern: The regular expression pattern to search for.
repl: The replacement string to substitute for occurrences of the pattern.
string: The input string in which to search for the pattern.
count (optional): Specifies the maximum number of replacements to make. If omitted or zero, all occurrences are replaced.
flags (optional): Optional flags that modify the behavior of the regex. Flags can be combined using the bitwise OR operator (|).
Here's how re.sub() works:

It searches the input string for all occurrences of the pattern.
For each occurrence found, it replaces it with the specified replacement string.
It returns a new string with the replacements applied.

'''
import re

pattern = r'\d+'  # Matches one or more digits
replacement = 'X'
string = 'I have 3 apples and 5 oranges'

result = re.sub(pattern, replacement, string)

print(result)  # Output: I have X apples and X oranges
