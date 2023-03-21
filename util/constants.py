from baseconv import BASE16_ALPHABET, BASE62_ALPHABET, BaseConverter


base16_alphabet = BASE16_ALPHABET.lower()
base64_alphabet = BASE62_ALPHABET + '._'
base16 = BaseConverter(base16_alphabet)
base64 = BaseConverter(base64_alphabet)
