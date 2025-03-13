def is_palindrome(s: str) -> bool:
    s = s.replace(" ", "").lower()
    return True if s == s[::-1] else False

print(is_palindrome("aba"))