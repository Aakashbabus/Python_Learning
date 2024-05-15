'''
In regular expressions, certain special characters have specific meanings that allow for more precise pattern matching.
These characters are often used in combination with functions like re.findall() to search for patterns within strings.
Here's an explanation of some commonly used special characters:

^: Matches the beginning of a line.

Example: ^hello matches "hello" only if it appears at the beginning of a line.
$: Matches the end of a line.

Example: world$ matches "world" only if it appears at the end of a line.
.: Matches any single character except newline characters.

Example: h.t matches "hat", "hot", "hit", etc.
\d: Matches any digit (equivalent to [0-9]).

Example: \d+ matches one or more consecutive digits.
\D: Matches any non-digit character (equivalent to [^0-9]).

Example: \D+ matches one or more consecutive non-digit characters.
\s: Matches any whitespace character (including spaces, tabs, and newline characters).

Example: \s+ matches one or more consecutive whitespace characters.
\S: Matches any non-whitespace character (equivalent to [^ \t\n\r\f\v]).

Example: \S+ matches one or more consecutive non-whitespace characters.
These special characters can be used within regular expressions to create more flexible and precise patterns for
matching text. When used with re.findall(), they allow you to find all occurrences of a pattern that matches the
specified criteria within a given string. For example, re.findall(r'\d+', text) would find all sequences of
digits within the text.

Remember that regular expressions are case-sensitive by default, so re.findall() will only match patterns
that exactly match the specified regular expression unless you use flags to modify its behavior.

'''
import re
def demonstrate(pattern, text):
    print("Text:", text)
    print("Pattern:", pattern)

    # Positive check: Finding matches
    matches = re.findall(pattern, text)
    print("Positive matches:", matches)

    print()


# ^: Matches the beginning of a line.
pattern = r'^hello'
text = "hello world\nhello there"
demonstrate(pattern, text)
text = "bello world\nhello there"
demonstrate(pattern, text)

# $: Matches the end of a line.
pattern = r'there$'
text = "hello world\nhello there"
demonstrate(pattern, text)
text = "hello world\nhello here"
demonstrate(pattern, text)

# .: Matches any single character except newline characters.
pattern = r'h.t'
text = "hat hot hit"
demonstrate(pattern, text)

# \d: Matches any digit (equivalent to [0-9]).
pattern = r'\d+'
text = "The number is 123"
demonstrate(pattern, text)

# \D: Matches any non-digit character (equivalent to [^0-9]).
pattern = r'\D+'
text = "The number is 123"
demonstrate(pattern, text)

# \s: Matches any whitespace character (including spaces, tabs, and newline characters).
pattern = r'\s+'
text = "Hello\tworld\nHow are you?"
demonstrate(pattern, text)

# \S: Matches any non-whitespace character (equivalent to [^ \t\n\r\f\v]).
pattern = r'\S+'
text = "Hello\tworld\nHow are you?"
demonstrate(pattern, text)
