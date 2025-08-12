def is_palindrome(s):
    # Normalize: lowercase and remove non-alphanumeric characters
    import re
    normalized = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    return normalized == normalized[::-1]
print (is_palindrome("racecar"))
