import re


def demonstrate(pattern, text):
    print("Text:", text)
    print("Pattern:", pattern)

    # Positive check: Finding matches
    matches = re.findall(pattern, text)
    print("Positive matches:", matches)

    print()


# *: Matches zero or more occurrences of the preceding character.
pattern = r'ab*'
text = "ab abb abbb"
demonstrate(pattern, text)

# +: Matches one or more occurrences of the preceding character.
pattern = r'ab+'
text = "ab abb abbb"
demonstrate(pattern, text)

# (): Groups patterns together.
pattern = r'(ab)+'
text = "ab abb abab ababab"
demonstrate(pattern, text)

# ?: Matches zero or one occurrence of the preceding character.
pattern = r'ab?'
text = "ab abb aab"
demonstrate(pattern, text)
