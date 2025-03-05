from collections import deque

def is_palindrome(value: str) -> bool:
    if not isinstance(value, str):
        return False

    if value == "":
        return False
