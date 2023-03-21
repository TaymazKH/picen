def is_binary_string(string: str):
    if not isinstance(string, str):
        return False
    for c in string:
        if c != '0' and c != '1':
            return False
    return True
