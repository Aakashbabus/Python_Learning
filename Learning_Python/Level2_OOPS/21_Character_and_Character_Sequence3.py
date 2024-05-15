'''
Let's discuss the [ ] and { } special characters:

[ ]: Specifies a character class, allowing you to match any single character contained within the brackets.

Positive check: If any character within the brackets matches, it's considered a match.
Negative check: If none of the characters within the brackets match, it's considered a non-match.
{ }: Specifies the number of occurrences of the preceding character or group.

Positive check: If the specified number of occurrences matches, it's considered a match.
Negative check: If the specified number of occurrences doesn't match, it's considered a non-match.
Let's see examples demonstrating positive and negative checks for each of these:

'''
import re


def demonstrate(pattern, text):
    print("Text:", text)
    print("Pattern:", pattern)

    # Positive check: Finding matches
    matches = re.findall(pattern, text)
    print("Positive matches:", matches)

    print()


# []: Specifies a character class.
pattern = r'[aeiou]'  # Matches any vowel
text = "hello world"
demonstrate(pattern, text)

# {}: Specifies the number of occurrences.
pattern = r'a{2,3}'  # Matches 2 or 3 consecutive 'a's
text = "aabaa aa"
demonstrate(pattern, text)

'''
By observing the output, you can see the matches and non-matches for each pattern, 
allowing you to understand how these special characters function in regular expressions. 
Feel free to experiment with different patterns and texts to deepen your understanding!
'''