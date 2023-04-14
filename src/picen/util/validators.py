from ..util.constants import base16_alphabet, base64_alphabet


def is_length128_base2_string(string: str):
    return _is_base_n_string(string, '01') and len(string) == 128


def is_length32_base16_string(string: str):
    return _is_base_n_string(string, base16_alphabet) and len(string) == 32


def is_length22_base64_string(string: str):
    return _is_base_n_string(string, base64_alphabet) and len(string) == 22


def _is_base_n_string(string: str, alphabet: str):
    if not isinstance(string, str):
        return False
    for c in string:
        if c not in alphabet:
            return False
    return True
