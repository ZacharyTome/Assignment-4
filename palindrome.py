from collections import deque

def is_palindrome(value: str) -> bool:
    if not isinstance(value, str):
        return False

    if value == "":
        print(False)
        return False

    value = ''.join(char.lower() for char in value if char.isalnum())

    p = deque(value)

    while len(p) > 1:
        if p.popleft() != p.pop():
            print(False)
            return False

    print(True)
    return True
