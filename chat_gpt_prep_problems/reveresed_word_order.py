"""
Write a function that reverses the order of words in a given string. Words are separated by one or more spaces. The
function should return a new string with words in reverse order, but with only a single space separating them.
"""


def reverse_words(s: str) -> str:
    word_l = s.split()
    reversed_l = reversed(word_l)
    return " ".join(reversed_l)

print(reverse_words("  asadfa  sadfasd  "))