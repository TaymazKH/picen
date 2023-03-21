from util.constants import base16_alphabet, base64_alphabet


def is_base2_string(string: str):
    return _is_base_n_string(string, '01')


def is_base16_string(string: str):
    return _is_base_n_string(string, base16_alphabet)


def is_base64_string(string: str):
    return _is_base_n_string(string, base64_alphabet)


def _is_base_n_string(string: str, alphabet: str):
    if not isinstance(string, str):
        return False
    for c in string:
        if c not in alphabet:
            return False
    return True
