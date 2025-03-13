def is_palindrome(s: str) -> bool:
    return True if s == s[::-1] else False

print(is_palindrome("aba"))